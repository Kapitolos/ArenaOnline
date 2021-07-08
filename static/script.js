

function backgroundtoggle(enemy) {  
  enemyname = enemy;     
  const pageid = "body" + enemyname;
  document.getElementById('body').setAttribute('id', pageid);
} 

function anitoggle(idname) {
  console.log(idname);
  const animation = idname+"attack";
  console.log(animation);

}


 
function test() {
  console.log("Hello World");
}

