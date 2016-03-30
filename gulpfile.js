/*
* Dependencias
*/
var gulp = require('gulp'),
  concat = require('gulp-concat'),
  uglify = require('gulp-uglify');

/*
* Configuración de la tarea 'demo'
*/

gulp.task('jsBower', function () {
    gulp.src('static/bower_components/**/*.min.js')
    .pipe(concat('bowerComponents.js'))
    .pipe(uglify())
    .pipe(gulp.dest('build/js'))
});



gulp.task('jsCustom', function () {
  gulp.src('static/js/**/*.js')
    .pipe(concat('jsCustom.js'))
    .pipe(uglify())
    .pipe(gulp.dest('build/js'))
});


gulp.task('default', ['jsBower', 'jsCustom']);


/*
* Configuración de la tarea 'watch'
*/


gulp.task('watch', function () {
    gulp.watch('static/bower_components/**/*.min.js', ['jsBower']);
    gulp.watch('./sass/**/*.scss', ['sass']);
});