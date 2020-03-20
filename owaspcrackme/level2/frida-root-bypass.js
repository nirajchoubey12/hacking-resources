Java.perform(function(){
     //obtain reference of the activity currently running
     var mainActivity = Java.use("sg.vantagepoint.uncrackable2.MainActivity");
     //obtain reference of the function which needs to be called
     mainActivity.a.overload("java.lang.String").implementation = function (v0){

     console.log("Inside function a bypassed root detection"+v0);
     //return false;
     };
    
});

     
