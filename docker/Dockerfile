ARG CERT_FILE=none
ARG WITH_CERT=no
#First stage, start from alpine
FROM alpine:3 AS base
ENV DEBIAN_FRONTEND noninteractive

RUN apk add --update \
    alpine-sdk \
    fontconfig \
    font-noto-cjk \
    freetype \
    lua5.3 \
    perl \
    bash \
    python3 \
    py3-pip \
    libressl-dev \
    pipx \
    curl \
    gnupg \
    unzip \
    py3-certifi && \
    rm -rf /var/cache/apk/*

# Dockerfiles have no "if", so we create intermediate stages to match a variable.
# These stages set up necessary environment variables and copy custom CA authorities into
# the container. Helpful within a corporate environment with an intercepting proxy (e.g. Zscaler).

FROM base AS base_yes
# use the CERT_FILE parameter passed as a build-arg
#ARG CERT_FILE
#ENV SSL_CERT_DIR=/usr/local/share/ca-certificates
#COPY ${CERT_FILE} $SSL_CERT_DIR/
RUN update-ca-certificates
# define environment variables
ENV HTTPS_CA_DIR=$SSL_CERT_DIR
ENV REQUESTS_CA_BUNDLE=$SSL_CERT_DIR/$CERT_FILE
ENV GIT_SSL_CAPATH=$REQUESTS_CA_BUNDLE
ENV GIT_SSL_CAINFO=$GIT_SSL_CAPATH
ENV CURL_CA_BUNDLE=$REQUESTS_CA_BUNDLE

FROM base AS base_no

#Install opentype fonts
FROM base_${WITH_CERT} as font_base

WORKDIR /fonts
ENV DEBIAN_FRONTEND noninteractive

#download the Adobe Source fonts referenced by 5.0/en/0x00-Header.yaml
RUN for font in source-sans source-serif source-code-pro; do \
	git_tarball_url="https://www.github.com/adobe-fonts/${font}"$(curl -L "https://github.com/adobe-fonts/${font}/tags" |  \
		     grep -o "/archive/refs/tags/.*\.zip" | grep -v 'variable' | sort -r | head -1 |tr -d '\n'); \
     echo "DOWNLOADING FROM: ${git_tarball_url}"; \
     curl -L --retry 5 "${git_tarball_url}" --output "$font.zip"; \
     unzip "${font}.zip" ; \
    done
RUN mkdir adobe-fonts
RUN find $PWD/ -name "*.ttf" -exec install -m644 {} adobe-fonts/ \; || return 1
RUN rm -rf $PWD/source*

FROM base_${WITH_CERT} as pandoc_base

# Install the Python dependency system-wide so the export tooling can import it
# regardless of which UID the container runs as (CI passes --user $(id -u)).
RUN pip3 install --no-cache-dir --break-system-packages dicttoxml2 setuptools

#install Pandoc
RUN adduser -s /bin/bash -g "pandoc" -D pandoc

RUN curl --output /tmp/pandoc.tar.gz -L https://github.com/jgm/pandoc/releases/download/2.19.2/pandoc-2.19.2-linux-amd64.tar.gz \
            && tar xvzf /tmp/pandoc.tar.gz --strip-components 1 -C /usr/local/ \
            && rm /tmp/pandoc.tar.gz

# verify pandoc installed correctly
RUN pandoc --version

# install as pandoc
USER pandoc

# setup workdir
WORKDIR /home/pandoc

# Install Lua Filters for pandoc
RUN curl --output /tmp/lua-filters.tar.gz -L https://github.com/pandoc/lua-filters/releases/latest/download/lua-filters.tar.gz  \
    && mkdir /home/pandoc/.pandoc \
    && tar xzf /tmp/lua-filters.tar.gz --strip-components=1 --one-top-level=/home/pandoc/.pandoc/ \
    && rm /tmp/lua-filters.tar.gz

FROM pandoc_base as tinytex_base

#Install tinyTex
# setup path
ENV PATH=/home/pandoc/.TinyTeX/bin/x86_64-linuxmusl/:$PATH
ENV TINY_TEX_VERSION=v0.45
RUN curl -L "https://raw.githubusercontent.com/rstudio/tinytex/${TINY_TEX_VERSION}/tools/install-bin-unix.sh" | sed -e 's/wget -qO-/curl -sL/' -e "s#\(sh -s\)#sed 's/wget/curl -LO/' | \1#" -e 's/retry-connrefused/tries 20/' > "install-unx.sh" \
	&& chmod +x install-unx.sh
RUN for i in 1 2 3 4 5; do bash -c "./install-unx.sh" && break || sleep 15; done && rm install-unx.sh

FROM tinytex_base as latex_base

# add tlmgr to path
RUN /home/pandoc/.TinyTeX/bin/*/tlmgr path add

# verify tlmgr version and add the packages needed to build the documents
RUN tlmgr --version
RUN for i in 1 2 3 4 5; do tlmgr update --self && break || sleep 15; done
RUN for i in 1 2 3 4 5; do tlmgr install \
    xecjk \
    ctex \
    fancyhdr \
    ragged2e \
    koma-script \
    setspace \
    colortbl \
    footnotebackref \
    polyglossia \
    pagecolor \
    csquotes \
    caption \
    mdframed \
    needspace \
    titling \
    bookmark \
    newunicodechar \
    adjustbox \
    collectbox \
    listings \
    background \
    bidi \
    everypage \
    footmisc \
    fvextra \
    ly1 \
    mweights \
    ucharcat \
    ulem \
    upquote \
    xurl \
    awesomebox \
    fontawesome5 \
    zref && break || sleep 15; done

FROM latex_base as work_layer
#copy fonts from font_base
USER root
COPY --from=font_base /fonts/adobe-fonts /usr/share/fonts/opentype/adobe-fonts
RUN fc-cache -f -v "/usr/share/fonts/opentype/adobe-fonts"

# Allow xelatex/luaotfload to write their font caches at runtime under any UID.
ENV TEXMFVAR=/tmp/texmf-var
ENV XDG_CACHE_HOME=/tmp/cache
RUN mkdir -p /tmp/texmf-var /tmp/cache && chmod -R 777 /tmp/texmf-var /tmp/cache

#setup the working dir for running make and creating the files
WORKDIR /data
VOLUME /data

#setup default action
ENTRYPOINT ["/scripts/run.sh"]
