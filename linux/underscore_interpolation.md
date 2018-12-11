# Underscore Interpolation in Shell

[From StackOverflow](https://stackoverflow.com/questions/17622106/variable-interpolation-in-shell)

> _ is a valid character in identifiers. Dot is not, so the shell tried to interpolate $filepath_newstap.

```
"$filepath"_newstap.sh
${filepath}_newstap.sh
$filepath\_newstap.sh
```