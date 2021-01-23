#!/bin/bash
#
# Once run the script, no need to run ./install.sh for testing. ;)
# Without an argument, this will install only normal variant.
# Valid arguments are:
#
#   compact dark dark-compact light light-compact all uninstall
#
# FIXME: `unity` and `xfwm4` are not fully supported for now since `*.svg` link incorrect locales (with '-light' variant).
# FIXME: Multiple arguments should be allowed.
set -ueo pipefail

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
SRC_DIR="$REPO_DIR/src"

DEST_DIR="$HOME/.themes"
THEME_NAME="Materia.dev"
# shellcheck disable=SC2034 # will this be used later?
COLOR_VARIANTS=('' '-dark' '-light')
# shellcheck disable=SC2034 # will this be used later?
SIZE_VARIANTS=('' '-compact')

GTK_VERSIONS=('3.0')
GS_VERSIONS=('3.18' '3.24' '3.26' '3.28' '3.30')
LATEST_GS_VERSION="${GS_VERSIONS[-1]}"

# Set a proper gnome-shell theme version
if [[ "$(which gnome-shell 2> /dev/null)" ]]; then
  CURRENT_GS_VERSION="$(gnome-shell --version | cut -d ' ' -f 3 | cut -d . -f -2)"
  for version in "${GS_VERSIONS[@]}"; do
    if (( "$(bc <<< "$CURRENT_GS_VERSION <= $version")" )); then
      GS_VERSION="$version"
      break
    elif (( "$(bc <<< "$CURRENT_GS_VERSION > $LATEST_GS_VERSION")" )); then
      GS_VERSION="$LATEST_GS_VERSION"
      break
    fi
  done
else
  GS_VERSION="$LATEST_GS_VERSION"
fi

test() {
  local color="$1"
  local size="$2"

  [[ "$color" == '-dark' ]] && local ELSE_DARK="$color"
  [[ "$color" == '-light' ]] && local ELSE_LIGHT="$color"

  local THEME_DIR="${DEST_DIR:?}/$THEME_NAME$color$size"

  # SC2115: Protect /.
  [[ -d "$THEME_DIR" ]] && rm -rf "${THEME_DIR:?}"

  mkdir -p                                                                      "$THEME_DIR"
  ln -sT "$SRC_DIR/index$color$size.theme"                                      "$THEME_DIR/index.theme"

  mkdir -p                                                                      "$THEME_DIR/cinnamon"
  ln -s  "$SRC_DIR/cinnamon/assets"                                             "$THEME_DIR/cinnamon"
  ln -s  "$SRC_DIR/cinnamon/thumbnail.png"                                      "$THEME_DIR/cinnamon"
  ln -sT "$SRC_DIR/cinnamon/cinnamon$color$size.css"                            "$THEME_DIR/cinnamon/cinnamon.css"

  mkdir -p                                                                      "$THEME_DIR/gnome-shell"
  ln -s  "$SRC_DIR/gnome-shell/"{extensions,pad-osd.css,process-working.svg}    "$THEME_DIR/gnome-shell"
  ln -sT "$SRC_DIR/gnome-shell/assets${ELSE_DARK:-}"                            "$THEME_DIR/gnome-shell/assets"
  ln -sT "$SRC_DIR/gnome-shell/$GS_VERSION/gnome-shell$color$size.css"          "$THEME_DIR/gnome-shell/gnome-shell.css"

  mkdir -p                                                                      "$THEME_DIR/gtk-2.0"
  ln -s  "$SRC_DIR/gtk-2.0/"{apps.rc,hacks.rc,main.rc}                          "$THEME_DIR/gtk-2.0"
  ln -sT "$SRC_DIR/gtk-2.0/assets${ELSE_DARK:-}"                                "$THEME_DIR/gtk-2.0/assets"
  ln -sT "$SRC_DIR/gtk-2.0/gtkrc$color"                                         "$THEME_DIR/gtk-2.0/gtkrc"

  for version in "${GTK_VERSIONS[@]}"; do
    mkdir -p                                                                    "$THEME_DIR/gtk-$version"
    ln -s  "$SRC_DIR/gtk/assets"                                                "$THEME_DIR/gtk-$version"
    ln -sT "$SRC_DIR/gtk/$version/gtk$color$size.css"                           "$THEME_DIR/gtk-$version/gtk.css"
    [[ "$color" != '-dark' ]] && \
    ln -sT "$SRC_DIR/gtk/$version/gtk-dark$size.css"                            "$THEME_DIR/gtk-$version/gtk-dark.css"
  done

  mkdir -p                                                                      "$THEME_DIR/metacity-1"
  ln -s  "$SRC_DIR/metacity-1/"{assets,metacity-theme-3.xml}                    "$THEME_DIR/metacity-1"
  ln -sT "$SRC_DIR/metacity-1/metacity-theme-2${ELSE_LIGHT:-}.xml"              "$THEME_DIR/metacity-1/metacity-theme-2.xml"

  mkdir -p                                                                      "$THEME_DIR/unity"
  ln -s  "$SRC_DIR/unity/"{*.svg,*.png,dash-widgets.json}                       "$THEME_DIR/unity"
  ln -sT "$SRC_DIR/unity/assets${ELSE_LIGHT:-}"                                 "$THEME_DIR/unity/assets"

  mkdir -p                                                                      "$THEME_DIR/xfwm4"
  ln -s  "$SRC_DIR/xfwm4/"{*.svg,themerc}                                       "$THEME_DIR/xfwm4"
  ln -sT "$SRC_DIR/xfwm4/assets${ELSE_LIGHT:-}"                                 "$THEME_DIR/xfwm4/assets"

  echo "Installed to '$THEME_DIR'"
}

case "${1:-}" in
  "")
    test '' ''
    ;;
  compact)
    test '' '-compact'
    ;;
  dark)
    test '-dark' ''
    ;;
  dark-compact)
    test '-dark' '-compact'
    ;;
  light)
    test '-light' ''
    ;;
  light-compact)
    test '-light' '-compact'
    ;;
  all)
    test '' ''
    test '' '-compact'
    test '-dark' ''
    test '-dark' '-compact'
    test '-light' ''
    test '-light' '-compact'
    ;;
  uninstall)
    # SC2115: Protect /.
    rm -rf "${DEST_DIR:?}/$THEME_NAME"{,-compact,-dark,-dark-compact,-light,-light-compact}
    ;;
  *)
    echo "Invalid argument: '${1:-}'"
    echo "Valid arguments are: 'compact' 'dark' 'dark-compact' 'light' 'light-compact' 'all' 'uninstall'"
    ;;
esac
