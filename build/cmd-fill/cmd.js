(()=>{
/* Animated "silk" fill inside the ⌘ logo (.cmk). One WebGL canvas renders the
   fill and is copied into each visible logo. Pauses off screen and in hidden
   tabs; draws one still frame for prefers-reduced-motion. */
const RM=matchMedia("(prefers-reduced-motion: reduce)"),N=160,live=new Set();
let gl,G,U,T0=performance.now(),raf=0,last=0;
const FS=`precision mediump float;uniform float t;varying vec2 v;
mat2 R(float a){float c=cos(a),s=sin(a);return mat2(c,-s,s,c);}
float th(float x){float e=exp(2.*clamp(x,-9.,9.));return (e-1.)/(e+1.);}
float b(vec2 p,vec2 c,float r){vec2 q=p-c;return exp(-dot(q,q)/(r*r));}
void main(){
 vec2 p=R(t*.42+.5*sin(t*.31))*v*1.15;
 float k=1.5+.5*sin(t*.53),o=.25*sin(t*.67);
 float h=th(k*p.x+o),y=.55*h+.18*sin(t*.4+p.x*1.3),g=.55*k*(1.-h*h);
 float d=(p.y-y)/sqrt(1.+g*g);
 vec2 c1=vec2(-.15+.25*sin(t*.5),.35+.15*cos(t*.37)),c2=vec2(.25+.2*cos(t*.45),-.4+.15*sin(t*.6));
 float up=step(0.,d),ad=abs(d);
 float bo=b(p,c1,.9)*exp(-ad*1.6),bv=b(p,c2,.78)*exp(-ad*2.2);
 vec3 org=mix(vec3(1.,.55,.28),vec3(1.,.22,.12),exp(-ad*9.));
 vec3 vio=mix(vec3(.55,.36,1.),vec3(.78,.12,.62),exp(-ad*10.));
 float tail=exp(-ad*70.)*(.55+.45*sin(p.x*2.+t))*.8;
 float ao=up*clamp(bo*1.25+tail*.7,0.,1.),av=(1.-up)*clamp(bv*1.3+tail*.6,0.,1.);
 float seam=smoothstep(.0,.035,ad);
 ao*=seam;av*=seam;
 vec3 col=org*ao+vio*av;float a=max(ao,av);
 gl_FragColor=vec4(col,a);}`;
function init(){
 G=document.createElement("canvas");G.width=G.height=N;
 gl=G.getContext("webgl",{premultipliedAlpha:true,alpha:true,antialias:false,preserveDrawingBuffer:true});
 if(!gl)return false;
 const sh=(ty,src)=>{const s=gl.createShader(ty);gl.shaderSource(s,src);gl.compileShader(s);return gl.getShaderParameter(s,gl.COMPILE_STATUS)?s:null};
 const vs=sh(gl.VERTEX_SHADER,"attribute vec2 a;varying vec2 v;void main(){v=a;gl_Position=vec4(a,0.,1.);}"),fs=sh(gl.FRAGMENT_SHADER,FS);
 if(!vs||!fs)return false;
 const pr=gl.createProgram();gl.attachShader(pr,vs);gl.attachShader(pr,fs);gl.linkProgram(pr);
 if(!gl.getProgramParameter(pr,gl.LINK_STATUS))return false;
 gl.useProgram(pr);gl.bindBuffer(gl.ARRAY_BUFFER,gl.createBuffer());
 gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,1,1]),gl.STATIC_DRAW);
 const l=gl.getAttribLocation(pr,"a");gl.enableVertexAttribArray(l);gl.vertexAttribPointer(l,2,gl.FLOAT,false,0,0);
 U=gl.getUniformLocation(pr,"t");gl.viewport(0,0,N,N);return true}
function draw(t){
 gl.uniform1f(U,t);gl.clearColor(0,0,0,0);gl.clear(gl.COLOR_BUFFER_BIT);gl.drawArrays(gl.TRIANGLE_STRIP,0,4);
 live.forEach(c=>{if(!c.isConnected){live.delete(c);return}const x=c.getContext("2d");x.clearRect(0,0,c.width,c.height);x.drawImage(G,0,0,c.width,c.height)})}
function loop(now){raf=0;if(document.hidden||!live.size||RM.matches)return;
 if(now-last>32){last=now;draw((now-T0)/1000+3.2)}raf=requestAnimationFrame(loop)}
const kick=()=>{if(!gl)return;if(RM.matches){draw(3.2);return}if(!raf&&live.size)raf=requestAnimationFrame(loop)};
const io="IntersectionObserver"in window?new IntersectionObserver(es=>{es.forEach(e=>e.isIntersecting?live.add(e.target):live.delete(e.target));kick()}):null;
let ok=null;
function mount(k){
 if(k.dataset.cmf)return;k.dataset.cmf=1;
 const f=document.createElement("i");f.className="cmf";f.setAttribute("aria-hidden","true");
 if(ok===null)ok=init();
 if(!ok){f.classList.add("nogl")}else{const c=document.createElement("canvas");c.width=c.height=Math.min(N,Math.round(110*Math.min(2,devicePixelRatio||1)));f.appendChild(c);io?io.observe(c):live.add(c)}
 k.appendChild(f);k.classList.add("cmon");kick()}
const scan=()=>document.querySelectorAll(".cmk:not([data-cmf])").forEach(mount);
new MutationObserver(scan).observe(document.documentElement,{childList:true,subtree:true});
document.addEventListener("visibilitychange",kick);RM.addEventListener&&RM.addEventListener("change",kick);
scan()})()
