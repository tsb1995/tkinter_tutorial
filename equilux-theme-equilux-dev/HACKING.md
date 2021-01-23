## Summary

- Do not edit the CSS directly, edit the source SCSS files and run `./parse-sass.sh`.
  - You'll need to have `sassc` installed.
- Do not edit the PNG directly, edit the source SVG files and run `./render-assets.sh`.
  - You'll need to have `inkscape` and `optipng` installed.
- To change the colors of SVG files, use a text editor instead of a image editor.

## How to tweak the theme

### SCSS

Like the upstream Adwaita, Materia is a complex theme, so to keep it
maintainable it's written and processed in Sass.

Here's a rundown of the "supporting" stylesheets, that are unlikely to be the
right place for a drive by stylesheet fix:

| File | Description |
| :-- | :-- |
| `_variables.scss` | Variables to allow easier definition of widget sizing/styling. |
| `_color-palette.scss` | Material Design color palette definitions. We don't recommend editing this unless Google updates the color scheme. |
| `_colors.scss` | Global color definitions. We keep the number of defined colors to a necessary minimum. It covers both the light variant and the dark variant. |
| `_colors-public.scss` | SCSS colors exported through gtk to allow for 3rd party apps color mixing. |
| `_drawing<-version>.scss` | Drawing helper mixings/functions to allow easier definition of widget drawing under specific context. |
| `_common<-version>.scss` | Actual definitions of style for each widget. This is where you are likely to add/remove your changes. |
| `_apps<-version>.scss` <br> `_extensions.scss` | App/extension specific stylings. |

You can read about Sass on its [web page](http://sass-lang.com/documentation/).
Once you make your changes to the SCSS files, run the `./parse-sass.sh` script
to rebuild the CSS files.

### SVG

In Materia, to keep it maintainable, SVG files are basically edited on
text-based. So if you just want to change the colors of SVG files, it is
recommended to use a **text editor** instead of a image editor.

Several SVG files are used to render the PNG assets. Once you make your changes
to the SVG files, run the `./render-assets.sh` script to render the PNG assets.

## How to change the color scheme

### Script

To easily change the color scheme, you can use the `change_color.sh` script (or
just use the [oomox](https://github.com/themix-project/oomox) app).

> Originally, `change_color.sh` and `scripts/*.sh` were implemented for oomox,
but you can also run it on the command line without the app.

> Note: This script doesn't support Chrome extensions for now.

For example, to change the color scheme to the previous Flat-Plat, run the
script as follows:

For `bash`:

```bash
./change_color.sh -o Flat-Plat <(echo -e "BG=F5F5F5\nFG=212121\nTXT_BG=FFFFFF\nTXT_FG=212121\nBTN_BG=FAFAFA\nBTN_FG=616161\nMENU_BG=455A64\nMENU_FG=FFFFFF\nSEL_BG=42A5F5\nSEL_FG=FFFFFF\nACCENT_BG=FF4081\nMATERIA_STYLE_COMPACT=False\n")
```

For `fish`:

```fish
./change_color.sh -o Flat-Plat (echo -e "BG=F5F5F5\nFG=212121\nTXT_BG=FFFFFF\nTXT_FG=212121\nBTN_BG=FAFAFA\nBTN_FG=616161\nMENU_BG=455A64\nMENU_FG=FFFFFF\nSEL_BG=42A5F5\nSEL_FG=FFFFFF\nACCENT_BG=FF4081\nMATERIA_STYLE_COMPACT=False\n" | psub)
```

### Manual

If you want to change the color scheme in more detail, edit the files where
colors are defined.

#### SCSS

- `src/_sass/_color-palette.scss`
- `src/_sass/_colors.scss`

> Note: Do not forget to run `./parse-sass.sh` after changing the colors of SCSS
files.

#### SVG

- `src/gtk/assets.svg`
- `src/gtk-2.0/assets{,-dark}.svg`
- `src/gnome-shell/assets{,-dark}/*.svg`
- `src/unity/*.svg`
- `src/unity/assets{,-light}/*.svg`
- `src/xfwm4/assets{,-light}/*.svg`
- `src/chrome/chrome-scrollbar{,-dark}/icons/*.svg`
- `src/chrome/chrome-theme{,-dark,-light}/*.svg`

> Note: Do not forget to run `./render-assets.sh` after changing the colors of
`src/gtk/assets.svg` and `src/gtk-2.0/assets{,-dark}.svg`.

#### Misc

- `src/gtk-2.0/gtkrc{,-dark,-light}`
- `src/metacity-1/metacity-theme-2{,-light}.xml`
- `src/xfwm4/assets{,-light}/themerc`
- `src/chrome/chrome-theme{,-dark,-light}/manifest.json`

> Note: The colors of `manifest.json` are defined in RGB format, so you need to
convert your colors from HEX format to RGB format.

After all the steps, run `./install.sh` to rebuild the themes.

## Useful Links

### Upstream theme sources

- [GTK+ 4.0](https://gitlab.gnome.org/GNOME/gtk/tree/master/gtk/theme/Adwaita) (master)
- [GTK+ 3](https://gitlab.gnome.org/GNOME/gtk/tree/gtk-3-24/gtk/theme/Adwaita) (3.24)
- [GTK+ 2](https://gitlab.gnome.org/GNOME/gnome-themes-extra/tree/master/themes/Adwaita/gtk-2.0)
- [GNOME Shell](https://gitlab.gnome.org/GNOME/gnome-shell/tree/master/data/theme)
  - [Sass sources](https://gitlab.gnome.org/GNOME/gnome-shell-sass) (legacy)
- [Metacity](https://gitlab.gnome.org/GNOME/gnome-themes-extra/tree/gnome-3-14/themes/Adwaita/metacity-1) (legacy)

> For other upstream theme sources of apps/DEs, see the comments in the source code.

### Tips

- [Material Design Guidelines](https://www.material.io/guidelines/)
- [CSS Guidelines for Materia](https://github.com/nana-4/materia-theme/wiki/CSS-Guidelines)
- [The GTK+ Inspector](https://blog.gtk.org/2017/04/05/the-gtk-inspector/)
- [Theming in GTK+ 4](https://developer.gnome.org/gtk4/stable/theming.html)
- [Theming in GTK+ 3](https://developer.gnome.org/gtk3/stable/theming.html)
- [GTK+ 2 Theming Tutorial](https://wiki.gnome.org/Attic/GnomeArt/Tutorials/GtkThemes)
- [The Pixmap Engine](https://wiki.gnome.org/Attic/GnomeArt/Tutorials/GtkEngines/PixmapEngine)
- [Designing Metacity Themes](https://wiki.gnome.org/Attic/GnomeArt/Tutorials/MetacityThemes)
- [Unity/Theming](https://wiki.ubuntu.com/Unity/Theming)
- [Xfwm4 theme how-to](https://wiki.xfce.org/howto/xfwm4_theme)
- [Chrome Themes](https://developer.chrome.com/extensions/themes)
