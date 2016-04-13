/*
* Dependencias
*/
var gulp = require('gulp');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var useref = require('gulp-useref');
var gulpif = require('gulp-if');
/*
* Configuración de la tarea 'demo'
*/
var destFolder = 'static'


gulp.task('minifiedjs', function () {
    return gulp.src('templates/partials/js.html')

        .pipe(useref({ searchPath: './' }))
        .pipe(gulpif('*.js', uglify()))
        .pipe(gulp.dest('static'));
});



gulp.task('build', ['minifiedjs']);
gulp.task('default', function (){});

/*
* Configuración de la tarea 'watch'
*/


gulp.task('watch', function () {
    gulp.watch('static/bower_components/**/*.min.js', []);
    gulp.watch('./sass/**/*.scss', ['sass']);
});