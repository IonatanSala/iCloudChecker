angular.module('app.services', [])

.factory('GetIphoneInformationService', ['$http', '$q',
	function($http, $q) {

	var apiEndpoint = "https://icloud-checker.herokuapp.com/";

	function getIphone(imei) {
		var q = $q.defer();

		$http.get(apiEndpoint + imei).then(function(data) {
			q.resolve(data.data);
		}).catch(function(err) {
			q.reject(err);
		});

		return q.promise;
	}

	return {
		getIphoneData: getIphone
	};



}])

.service('BlankService', [function(){

}]);

