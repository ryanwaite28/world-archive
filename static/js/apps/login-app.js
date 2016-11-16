var App = angular.module('loginApp' , []);

App.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[');
  $interpolateProvider.endSymbol(']}');
}]);

App.controller('loginCtrl' , ['$scope', function($scope){

  window.scope = $scope;

}]);
