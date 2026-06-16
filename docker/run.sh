#! /bin/bash
#
# Entrypoint for the TCASVS document builder image.
# Invoked by the root Makefile / CI with the source tree mounted at /data
# and this scripts directory mounted at /scripts.
#
set -e

case "$TARGET" in
  verify)
    make verify
    ;;
  clean)
    make clean
    ;;
  5.0 | "")
    if [ -n "$LANGS" ]; then
      export SELECTED_LANGS="$LANGS"
    fi
    make "${FORMATS:-all}"
    ;;
  *)
    make "${FORMATS:-all}"
    ;;
esac
