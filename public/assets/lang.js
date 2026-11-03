// Gợi ý ngôn ngữ – lưu lựa chọn trên máy người dùng, không gửi đi đâu
(function(){
  var k='dnt-lang', box=document.getElementById('lang-hint');
  function save(v){try{localStorage.setItem(k,v)}catch(e){}}
  document.querySelectorAll('[data-lang-set]').forEach(function(a){
    a.addEventListener('click',function(){save(a.getAttribute('data-lang-set'))});
  });
  if(!box) return;
  var saved=null; try{saved=localStorage.getItem(k)}catch(e){}
  var langs=navigator.languages||[navigator.language||''];
  var vi=langs.some(function(l){return String(l).toLowerCase().indexOf('vi')===0});
  if(saved==='vi'||(!saved&&vi)) return;
  box.hidden=false;
  var stay=document.getElementById('lang-stay');
  if(stay) stay.addEventListener('click',function(){save('vi');box.hidden=true});
})();
