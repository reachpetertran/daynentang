// Gợi ý ngôn ngữ – lưu lựa chọn trên máy người dùng, không gửi đi đâu
(function(){
  var k='dnt-lang', box=document.getElementById('lang-hint');
  function save(v){try{localStorage.setItem(k,v)}catch(e){}}
  document.querySelectorAll('[data-lang-set]').forEach(function(a){
    a.addEventListener('click',function(){save(a.getAttribute('data-lang-set'))});
  });
  if(!box) return;
  function show(){
    box.hidden=false;
    var stay=document.getElementById('lang-stay');
    if(stay) stay.addEventListener('click',function(){save('vi');box.hidden=true});
  }
  var saved=null; try{saved=localStorage.getItem(k)}catch(e){}
  if(saved==='vi') return;
  if(saved==='en') return show();
  var langs=navigator.languages||[navigator.language||''];
  if(langs.some(function(l){return String(l).toLowerCase().indexOf('vi')===0})) return;
  if(!window.fetch) return;
  fetch('/api/vung',{cache:'no-store'}).then(function(r){return r.ok?r.json():null})
    .then(function(d){if(d&&d.vn===false) show();}).catch(function(){});
})();
