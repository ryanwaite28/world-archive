var App = angular.module('welcomeApp' , []);

App.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[');
  $interpolateProvider.endSymbol(']}');
}]);

App.controller('welcomeCtrl' , ['$scope', function($scope){

  window.scope = $scope;

}]);
