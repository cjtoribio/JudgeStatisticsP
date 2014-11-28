angular.module('JudgeStatsApp', ['ngResource', 'ngMessages', 'ngRoute', 'ngAnimate', 'mgcrea.ngStrap','angularCharts','infinite-scroll', 'ngCookies'])
  .config(function ($routeProvider, $locationProvider) {
//    $locationProvider.html5Mode(true);

    $routeProvider
      .when('/spoj/stats', {
        templateUrl: 'views/spoj/stats.html'
      })
      .when('/login', {
        templateUrl: 'views/login.html'
      })
      .otherwise({
        redirectTo: '/login'
      });
  });