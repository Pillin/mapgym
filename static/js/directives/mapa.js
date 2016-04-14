
function mapaDirective(BranchOfficeService) {
  var controllerFunction = function () {

  };

  var linkFunction = function ($scope, element, attrs) {
    $scope.map = { center: { latitude: -33.4319495, longitude: -70.6209137 }, zoom: 15 };
    $scope.randomMarkers = [];


    $scope.getMarkers = function () {
      BranchOfficeService.query({}).success(
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
                slug: elem.slug,
                title: elem.name,
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
    templateUrl: 'static/templates/mapa.html',
    controller: controllerFunction, //Embed a custom controller in the directive
    link: linkFunction //DOM manipulation
  }
}

angular
  .module( 'gym.directive', [])
  .directive( 'mapa', ['BranchOfficeService', mapaDirective])
