angular.module('JudgeStatsApp')
.factory('LoginService', function($resource, $cookieStore, $http, Base64, $rootScope) {
	var LoginService = {};
	
	LoginService.authData = $cookieStore.get('authData');
	if(LoginService.authData == null){
		LoginService.authData = { token: '', username: null };
	}
	$http.defaults.headers.common.Authorization = 'Basic ' + LoginService.authData.token;
	
	LoginService.saveCredentials = function(data){
		LoginService.clearCredentials();
		for(var i in data) LoginService.authData[i] = data[i];
        $http.defaults.headers.common.Authorization = 'Basic ' + LoginService.authData.token;
        $cookieStore.put('authData', LoginService.authData);
	};
	LoginService.clearCredentials = function(){
		$http.defaults.headers.common.Authorization = 'Basic ';
		$cookieStore.remove('authData');
		for(var i in LoginService.authData)
			delete LoginService.authData[i];
	};
	
	LoginService.login = function(credentials , callback) {
		$resource('/user/getToken').save({
			username: credentials.username,
			password: credentials.password
		}, function(data) {
			data.token = Base64.encode(':' + data.token);
			LoginService.saveCredentials(data);
			if(callback)callback(data);
		}, function(error) {            
			console.log(error);
		});
	};
	
	LoginService.logOut = function(credentials, callback) {
		LoginService.clearCredentials();
	};
	

	LoginService.verifyToken = function(callback) {
		$http.get('/user/getToken')
		.success(function(data, status) {
			callback(data, status);
		})
		.error(function(error, status){
			callback(null, status);
		});
	};
	

	LoginService.getUser = function(callback) {
		$http.get('/user/getToken')
		.success(function(data, status) {
			callback(data, status);
		})
		.error(function(error, status){
			callback(null, status);
		});
	};
	
	LoginService.isOnline = function(){
		return LoginService.authData.isOnline == true;
	};
	  
	return LoginService;
})

.factory('Base64', function () {
    /* jshint ignore:start */
  
    var keyStr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';
  
    return {
        encode: function (input) {
            var output = "";
            var chr1, chr2, chr3 = "";
            var enc1, enc2, enc3, enc4 = "";
            var i = 0;
  
            do {
                chr1 = input.charCodeAt(i++);
                chr2 = input.charCodeAt(i++);
                chr3 = input.charCodeAt(i++);
  
                enc1 = chr1 >> 2;
                enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
                enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
                enc4 = chr3 & 63;
  
                if (isNaN(chr2)) {
                    enc3 = enc4 = 64;
                } else if (isNaN(chr3)) {
                    enc4 = 64;
                }
  
                output = output +
                    keyStr.charAt(enc1) +
                    keyStr.charAt(enc2) +
                    keyStr.charAt(enc3) +
                    keyStr.charAt(enc4);
                chr1 = chr2 = chr3 = "";
                enc1 = enc2 = enc3 = enc4 = "";
            } while (i < input.length);
  
            return output;
        },
  
        decode: function (input) {
            var output = "";
            var chr1, chr2, chr3 = "";
            var enc1, enc2, enc3, enc4 = "";
            var i = 0;
  
            // remove all characters that are not A-Z, a-z, 0-9, +, /, or =
            var base64test = /[^A-Za-z0-9\+\/\=]/g;
            if (base64test.exec(input)) {
                window.alert("There were invalid base64 characters in the input text.\n" +
                    "Valid base64 characters are A-Z, a-z, 0-9, '+', '/',and '='\n" +
                    "Expect errors in decoding.");
            }
            input = input.replace(/[^A-Za-z0-9\+\/\=]/g, "");
  
            do {
                enc1 = keyStr.indexOf(input.charAt(i++));
                enc2 = keyStr.indexOf(input.charAt(i++));
                enc3 = keyStr.indexOf(input.charAt(i++));
                enc4 = keyStr.indexOf(input.charAt(i++));
  
                chr1 = (enc1 << 2) | (enc2 >> 4);
                chr2 = ((enc2 & 15) << 4) | (enc3 >> 2);
                chr3 = ((enc3 & 3) << 6) | enc4;
  
                output = output + String.fromCharCode(chr1);
  
                if (enc3 != 64) {
                    output = output + String.fromCharCode(chr2);
                }
                if (enc4 != 64) {
                    output = output + String.fromCharCode(chr3);
                }
  
                chr1 = chr2 = chr3 = "";
                enc1 = enc2 = enc3 = enc4 = "";
  
            } while (i < input.length);
  
            return output;
        }
    };
  
    /* jshint ignore:end */
});