(()=>{
/* ⌘ logo in Siri colours (Krishna 2026-11-03). The hero/profile .cmk ⌘ becomes a bold solid ⌘ (CSS mask)
   filled with five drifting colour blobs (pink, violet, blue, cyan and the site's --ac yellow) that swirl
   in different directions, plus a soft glow of the same colours behind it. One WebGL canvas renders the
   colours and is copied into each logo. Pauses off screen / hidden tab; reduced motion = still frame. */
const RM=matchMedia("(prefers-reduced-motion: reduce)"),N=128,live=new Set();
let gl,G,U,raf=0,last=0,fr=0;const T0=performance.now();
const FS=`precision mediump float;uniform float t;uniform vec3 acc;varying vec2 v;
vec3 siri(vec2 p,float t){
 vec2 q=p+.28*vec2(sin(p.y*2.3+t*.7),cos(p.x*2.1-t*.6));
 q+=.16*vec2(sin(q.y*3.7-t*.9),cos(q.x*3.3+t*.8));
 vec3 C[5];C[0]=vec3(1.,.18,.56);C[1]=vec3(.62,.25,1.);C[2]=vec3(.12,.45,1.);C[3]=vec3(.1,.9,1.);C[4]=acc;
 vec3 acc=vec3(0.);float w=0.;
 for(int i=0;i<5;i++){float f=float(i);
  vec2 c=.75*vec2(sin(t*(.31+.07*f)+f*1.7),cos(t*(.27+.05*f)+f*2.9));
  float k=1./(.06+pow(length(q-c),2.2));acc+=C[i]*k;w+=k;}
 vec3 col=acc/w;
 float m=max(col.r,max(col.g,col.b));col=mix(vec3(dot(col,vec3(.3333))),col,1.35)/max(m,.001);
 return clamp(col,0.,1.);}
void main(){gl_FragColor=vec4(siri(v*.9,t),1.);}`;
function init(){G=document.createElement("canvas");G.width=G.height=N;
 gl=G.getContext("webgl",{alpha:false,antialias:false,preserveDrawingBuffer:true});if(!gl)return false;
 const sh=(ty,s)=>{const x=gl.createShader(ty);gl.shaderSource(x,s);gl.compileShader(x);return gl.getShaderParameter(x,gl.COMPILE_STATUS)?x:null};
 const vs=sh(gl.VERTEX_SHADER,"attribute vec2 a;varying vec2 v;void main(){v=a;gl_Position=vec4(a,0.,1.);}"),fs=sh(gl.FRAGMENT_SHADER,FS);if(!vs||!fs)return false;
 const pr=gl.createProgram();gl.attachShader(pr,vs);gl.attachShader(pr,fs);gl.linkProgram(pr);if(!gl.getProgramParameter(pr,gl.LINK_STATUS))return false;
 gl.useProgram(pr);gl.bindBuffer(gl.ARRAY_BUFFER,gl.createBuffer());gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,1,1]),gl.STATIC_DRAW);
 const l=gl.getAttribLocation(pr,"a");gl.enableVertexAttribArray(l);gl.vertexAttribPointer(l,2,gl.FLOAT,false,0,0);
 U={t:gl.getUniformLocation(pr,"t"),acc:gl.getUniformLocation(pr,"acc")};gl.viewport(0,0,N,N);return true}
const pc=document.createElement("i");pc.style.display="none";
function accent(){const k=[...live][0];if(!k)return;if(!pc.isConnected)document.body.appendChild(pc);
 const ac=getComputedStyle(k).getPropertyValue("--ac").trim()||"#ffc21a";pc.style.color=ac;
 const z=getComputedStyle(pc).color.match(/[\d.]+/g)||[255,194,26];gl.uniform3f(U.acc,z[0]/255,z[1]/255,z[2]/255)}
function draw(s){if(!(fr++%20))accent();gl.uniform1f(U.t,s);gl.drawArrays(gl.TRIANGLE_STRIP,0,4);
 live.forEach(c=>{if(!c.isConnected){live.delete(c);return}const x=c.getContext("2d");x.drawImage(G,0,0,c.width,c.height)})}
function loop(n){raf=0;if(document.hidden||!live.size||RM.matches)return;if(n-last>32){last=n;draw((n-T0)/1000+4)}raf=requestAnimationFrame(loop)}
const kick=()=>{if(!gl)return;if(RM.matches){fr=0;draw(4);return}if(!raf&&live.size)raf=requestAnimationFrame(loop)};
const io="IntersectionObserver"in window?new IntersectionObserver(es=>{es.forEach(e=>e.isIntersecting?live.add(e.target):live.delete(e.target));kick()}):null;
let ok=null;
function mount(k){if(k.dataset.cs)return;k.dataset.cs=1;if(ok===null)ok=init();
 const w=document.createElement("i");w.className="csw"+(ok?"":" nogl");w.setAttribute("aria-hidden","true");
 w.innerHTML='<i class="csg"><i class="csm"></i></i><i class="csm csf"></i>';
 if(ok)w.querySelectorAll(".csm").forEach(m=>{const c=document.createElement("canvas");c.width=c.height=N;m.appendChild(c);io?io.observe(c):live.add(c)});
 k.appendChild(w);k.classList.add("cson");kick()}
const scan=()=>document.querySelectorAll(".cmk:not([data-cs])").forEach(mount);
new MutationObserver(scan).observe(document.documentElement,{childList:true,subtree:true});
document.addEventListener("visibilitychange",kick);RM.addEventListener&&RM.addEventListener("change",kick);scan()})()