function renderFeatured(){
  const f = DIGGING_BRITANNIA.featuredFind;
  const img = document.querySelector("#featured-image");
  if(!img) return;
  img.src = f.image;
  img.alt = f.title;
  document.querySelector("#featured-title").textContent = f.title;
  document.querySelector("#featured-subtitle").textContent = f.subtitle;
  document.querySelector("#featured-description").textContent = f.description;
  document.querySelector("#featured-meta").innerHTML = f.details.map(([k,v]) =>
    `<div><strong>${k}</strong>${v}</div>`).join("");
}
function renderEvents(){
  const wrap = document.querySelector("#events-list");
  if(!wrap) return;
  wrap.innerHTML = DIGGING_BRITANNIA.events.map(e => `
    <article class="card event">
      <div class="event-date">${e.date}</div>
      <div><h3>${e.title}</h3><p><strong>${e.location}</strong></p><p>${e.description}</p></div>
    </article>`).join("");
}
function renderShowcase(){
  const wrap = document.querySelector("#showcase-list");
  if(!wrap) return;
  wrap.innerHTML = DIGGING_BRITANNIA.pastDigs.map(d => `
    <article class="card">
      <span class="tag">${d.date}</span><span class="tag">${d.location}</span>
      <h3>${d.title}</h3><p>${d.description}</p>
      <div class="gallery">${d.images.map(src => `<img src="${src}" alt="${d.title} find">`).join("")}</div>
    </article>`).join("");
}
function setupContact(){
  const form=document.querySelector("#contact-form");
  if(!form) return;
  form.addEventListener("submit", e=>{
    e.preventDefault();
    const data=new FormData(form);
    const subject=encodeURIComponent("Digging Britannia website enquiry");
    const body=encodeURIComponent(
      `Name: ${data.get("name")}\nEmail: ${data.get("email")}\n\n${data.get("message")}`
    );
    window.location.href=`mailto:${DIGGING_BRITANNIA.contactEmail}?subject=${subject}&body=${body}`;
  });
}
document.addEventListener("DOMContentLoaded",()=>{renderFeatured();renderEvents();renderShowcase();setupContact();});

// Mobile navigation
(function(){
  const toggle=document.querySelector('.menu-toggle');
  const nav=document.querySelector('#site-navigation');
  if(!toggle || !nav) return;
  toggle.addEventListener('click',()=>{
    const open=nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded',String(open));
    toggle.setAttribute('aria-label',open?'Close navigation':'Open navigation');
  });
  nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{
    nav.classList.remove('open');
    toggle.setAttribute('aria-expanded','false');
    toggle.setAttribute('aria-label','Open navigation');
  }));
  window.addEventListener('resize',()=>{
    if(window.innerWidth>850){
      nav.classList.remove('open');
      toggle.setAttribute('aria-expanded','false');
      toggle.setAttribute('aria-label','Open navigation');
    }
  });
})();
