/* Halftone Earth in Siri colours. sgGlobe(canvas,{src,cells,speed}) renders a turning
   globe as a screen-fixed dot grid: dot size follows the Earth map's brightness (clouds big,
   ocean small) and dot colour is a slowly flowing pink/violet/blue/cyan/orange gradient.
   On a light page it prints like ink (dark ocean = big dots, clouds = paper);
   on a dark page it glows (clouds = big dots). The orange blob follows the page's --ac accent (the site's yellow). Pauses off screen and in hidden tabs; reduced motion draws one still frame. */
window.sgGlobe=(cv,o={})=>{
 const pc=document.createElement("i");pc.style.display="none";document.body.appendChild(pc);
 const RM=matchMedia("(prefers-reduced-motion: reduce)"),gl=cv.getContext("webgl",{premultipliedAlpha:true,alpha:true,antialias:false});
 if(!gl){cv.classList.add("nogl");return}
 const FS=`precision highp float;uniform float t,cs,ink;uniform vec3 acc;uniform vec2 res;uniform sampler2D map;
const float PI=3.14159265;const float R=${(o.r||.78).toFixed(3)};
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
float lum(vec2 q){
 float r2=dot(q,q);if(r2>1.)return -1.;
 float z=sqrt(1.-r2);float tl=.38;
 vec3 s=vec3(q.x,q.y*cos(tl)+z*sin(tl),-q.y*sin(tl)+z*cos(tl));
 float lon=atan(s.x,s.z)+t*${(o.speed||.12).toFixed(3)},lat=asin(clamp(s.y,-1.,1.));
 float L=texture2D(map,vec2(fract(lon/(2.*PI)+.5),.5-lat/PI)).r;
 return clamp(mix(.07,1.,L)*mix(.5+.5*pow(z,.6),1.,ink),0.,1.);}
void main(){
 vec2 fc=gl_FragCoord.xy,c=(floor(fc/cs)+.5)*cs;
 vec2 p=(c/res*2.-1.)/R,pf=(fc/res*2.-1.)/R;
 float L=lum(p);vec3 col=siri(pf,t);
 float a=0.,halo=0.;
 if(L>=0.){float v=mix(L,pow(1.-L*.97,1.15),ink),d=length(fc-c)/cs,rad=mix(.56,.5,ink)*sqrt(v)+.04;col=mix(col,col*col*.85,ink*.6);a=1.-smoothstep(rad-1.2/cs,rad,d);halo=(1.-ink*.7)*.35*v*exp(-max(d-rad,0.)*6.);}
 float r=length(pf);
 float ga=atan(pf.y,pf.x);float wob=.035*sin(ga*3.+t*1.3)+.025*sin(ga*5.-t*1.7);
 float glow=(exp(-max(r-1.,0.)*(9.-60.*wob))*smoothstep(.9,1.,r)*smoothstep(1.27,1.06,r))*${(o.glow??.75).toFixed(3)}*(.8+.2*sin(ga*2.-t));
 vec3 gc=siri(pf*1.05,t+1.);float hl=halo*(1.-a);
 vec3 o=col*a+col*hl+gc*glow*(1.-a-hl);float A=clamp(a+hl+glow*(1.-a-hl),0.,1.);
 gl_FragColor=vec4(o,A);}`;
 const sh=(ty,s)=>{const x=gl.createShader(ty);gl.shaderSource(x,s);gl.compileShader(x);if(!gl.getShaderParameter(x,gl.COMPILE_STATUS))console.warn(gl.getShaderInfoLog(x));return x};
 const pr=gl.createProgram();gl.attachShader(pr,sh(gl.VERTEX_SHADER,"attribute vec2 a;void main(){gl_Position=vec4(a,0.,1.);}"));gl.attachShader(pr,sh(gl.FRAGMENT_SHADER,FS));gl.linkProgram(pr);
 if(!gl.getProgramParameter(pr,gl.LINK_STATUS)){cv.classList.add("nogl");return}
 gl.useProgram(pr);gl.bindBuffer(gl.ARRAY_BUFFER,gl.createBuffer());gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,1,1]),gl.STATIC_DRAW);
 const la=gl.getAttribLocation(pr,"a");gl.enableVertexAttribArray(la);gl.vertexAttribPointer(la,2,gl.FLOAT,false,0,0);
 const U={t:gl.getUniformLocation(pr,"t"),cs:gl.getUniformLocation(pr,"cs"),ink:gl.getUniformLocation(pr,"ink"),acc:gl.getUniformLocation(pr,"acc"),res:gl.getUniformLocation(pr,"res")};
 const tx=gl.createTexture();let ready=false,vis=true,raf=0,last=0;const T0=performance.now();
 const im=new Image();im.onload=()=>{gl.bindTexture(gl.TEXTURE_2D,tx);gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL,false);
  gl.texImage2D(gl.TEXTURE_2D,0,gl.LUMINANCE,gl.LUMINANCE,gl.UNSIGNED_BYTE,im);
  gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_MIN_FILTER,gl.LINEAR);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_MAG_FILTER,gl.LINEAR);
  gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_WRAP_S,gl.REPEAT);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_WRAP_T,gl.CLAMP_TO_EDGE);ready=true;size();kick()};
 im.onerror=()=>cv.classList.add("nogl");im.src=o.src;
 function size(){const d=Math.min(2,devicePixelRatio||1),w=Math.max(1,Math.round(cv.clientWidth*d));if(cv.width!==w){cv.width=cv.height=w;gl.viewport(0,0,w,w)}
  gl.uniform2f(U.res,w,w);gl.uniform1f(U.cs,Math.max(Math.round(2.5*d),Math.round(w/(o.cells||96))))}
 function theme(){const m=getComputedStyle(cv).color.match(/[\d.]+/g);const k=m?(.3*m[0]+.59*m[1]+.11*m[2])/255:1;gl.uniform1f(U.ink,k<.5?1:0);const ac=(getComputedStyle(cv).getPropertyValue("--ac")||"").trim();let rgb=[1,.55,.15];if(ac){pc.style.color=ac;const z=getComputedStyle(pc).color.match(/[\d.]+/g);if(z)rgb=z.slice(0,3).map(x=>x/255)}gl.uniform3f(U.acc,rgb[0],rgb[1],rgb[2])}
 let fr=0;function draw(s){if(!(fr++%20))theme();gl.uniform1f(U.t,s);gl.clearColor(0,0,0,0);gl.clear(gl.COLOR_BUFFER_BIT);gl.drawArrays(gl.TRIANGLE_STRIP,0,4)}
 function loop(n){raf=0;if(!vis||document.hidden||RM.matches)return;if(n-last>32){last=n;draw((n-T0)/1000+4)}raf=requestAnimationFrame(loop)}
 function kick(){if(!ready)return;if(RM.matches){draw(4);return}if(!raf&&vis)raf=requestAnimationFrame(loop)}
 "IntersectionObserver"in window&&new IntersectionObserver(e=>{vis=e[0].isIntersecting;kick()}).observe(cv);
 "ResizeObserver"in window&&new ResizeObserver(()=>{if(ready){size();RM.matches&&draw(4)}}).observe(cv);
 document.addEventListener("visibilitychange",kick);RM.addEventListener&&RM.addEventListener("change",kick);
};
