var App = angular.module('signupApp' , []);

App.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[');
  $interpolateProvider.endSymbol(']}');
}]);

App.controller('signupCtrl' , ['$scope', function($scope){

  window.scope = $scope;

}]);
