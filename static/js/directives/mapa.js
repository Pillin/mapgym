
function mapaDirective(BranchOfficeService) {
  var controllerFunction = function () {

  };

  var linkFunction = function ($scope, element, attrs) {
    $scope.map = { center: { latitude: -33.4319495, longitude: -70.6209137 }, zoom: 15 };
    $scope.randomMarkers = [];


    $scope.getMarkers = function () {
      BranchOfficeService.query().success(
        function(data){
          var information = data.filter(
            function (elem) {
              return elem.direction.lat
            }
          );
          $scope.randomMarkers = information.map(
            function (elem) {
              return {
                id: elem.id,
                title: elem.slug,
                latitude: elem.direction.lat,
                longitude: elem.direction.lng
              }
          });
 
      });
    }

    $scope.getMarkers();

  }

  return {
    restrict: 'E', //E = element, A = attribute, C = class, M = comment         
    scope: {
        //@ reads the attribute value, = provides two-way binding, & works with functions
    }, 
    template: "<ui-gmap-google-map center='map.center' zoom='map.zoom'><ui-gmap-markers ng-if='randomMarkers.length' models='randomMarkers' coords=\"'self'\" icon='icon'></ui-gmap-markers></ui-gmap-google-map>",
    controller: controllerFunction, //Embed a custom controller in the directive
    link: linkFunction //DOM manipulation
  }
}

angular
  .module( 'gym.directive', [])
  .directive( 'mapa', ['BranchOfficeService', mapaDirective])
