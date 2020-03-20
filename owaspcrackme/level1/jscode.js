Java.perform(function(){
     //obtain reference of the activity currently running
     var decryptClass = Java.use("sg.vantagepoint.a.a");

     decryptClass.a.implementation = function(v0, v1){

        //calling the function itself to get its return value
        var decrypt = this.a(v0,v1);

        var flag = "";

        //converting the returned byte array to ascii
        for(var i = 0; i < decrypt.length; i++) {
		flag += String.fromCharCode(decrypt[i]);
           }

       // Leaking our secret
        console.log(flag);
        return decrypt;
	}
    
});
