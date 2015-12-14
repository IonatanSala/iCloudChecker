angular.module('app.controllers', [])
  
.controller('iphoneCheckerCtrl', function($scope, GetIphoneInformationService, $ionicLoading) {
	$scope.getDetails = function(imei) {
		$ionicLoading.show({
		    template: 'Loading...'
		});
		GetIphoneInformationService.getIphoneData(imei).then(function(data) {
			console.log('success');
			$scope.phoneDetails = data;
			 $ionicLoading.hide();
		}).catch(function(err) {
			console.log('err');
			 $ionicLoading.hide();
		});
	}
	
})
   
.controller('resultsCtrl', function($scope) {

})
 