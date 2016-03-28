(function() {

    var module = angular.module('brandoffice.service',[]);

    module.factory('BranchOfficeService', ['GenericCRUDService',
        function(GenericCRUDService){
            var brandoffices = GenericCRUDService('', 'branch-office');
            return brandoffices;
        }
    ]);

})();