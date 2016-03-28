(function() {
    var module = angular.module('grud.services', []);
    module.factory('GenericCRUDService', ['$http','$resource',

    function($http, $resource) {

        var GenericCRUDService = {
            all: all,
            query: query,
            create: create,
            get: get,
            remove: remove,
            put: put,
            patch: patch,
            save: save,
            setModelService: setModelService,
            setModelServiceExpired: setModelServiceExpired
        };

        return function (prefix, model) {
            var GenericCRUDService_extended = $.extend({}, GenericCRUDService);
            GenericCRUDService_extended.model = model;
            GenericCRUDService_extended.prefix = prefix;
            return GenericCRUDService_extended;
        };

        function all(paginated) {
            paginated = !!paginated ? 1 : 0;
            return $http.get(this.prefix +'/api/' + this.model + '?paginated=' + paginated);
        }

        function query(params) {
            return $http.get(this.prefix + '/api/' + this.model, {params: params});
        }

        function create(object) {
            this.setModelServiceExpired();
            return $http.post(this.prefix + '/api/' + this.model, object);
        }

        function get(objectId) {
            return $http.get(this.prefix + '/api/' + this.model + '/' + objectId);
        }

        function remove(objectId) {
            this.setModelServiceExpired();
            return $http.delete(this.prefix + '/api/' + this.model + '/' + objectId);
        }

        function put(objectId, object) {
            this.setModelServiceExpired();
            return $http.put(this.prefix + '/api/' + this.model + '/' + objectId, object);
        }

        function patch(objectId, object) {
            this.setModelServiceExpired();
            return $http.patch(this.prefix + '/api/' + this.model + '/' + objectId, object);
        }

        function save(object) {
            if (object.id)
                return this.put(object.id, object);
            else
                return this.create(object);
        }

        function setModelService(service) {
            this.modelService = service;
        }

        function setModelServiceExpired() {
            if (this.modelService)
                this.modelService.expire();
        }
    }]);
})();
