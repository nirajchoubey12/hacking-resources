Java.perform(function(){

    console.log("\n Root detection bypass with frida");
    
    var postlogin = Java.use("com.android.insecurebankv2.PostLogin");

    postlogin.doesSUexist.implementation = function() {

        console("\ninside doesSuExist function");
        return false;
    }
    
    
    postlogin.doesSuperuserApkExist.implementation = function(v0){

        console.log("\n varaible passed"+v0);


        return false;

            };
});

//frida -U --no-pause -l root-bypass-frida.js -f com.android.insecurebankv2
