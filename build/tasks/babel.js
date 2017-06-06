var gulp = require("gulp");
var paths = require('../paths');
var sourcemaps = require("gulp-sourcemaps");
var babel = require("gulp-babel");

gulp.task("babel", function () {
  return gulp.src(paths.src)
    .pipe(sourcemaps.init())
    .pipe(babel())
    .pipe(sourcemaps.write("."))
    .pipe(gulp.dest("dist/src"));
});
