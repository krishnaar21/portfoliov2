/* Halftone Earth in Siri colours. sgGlobe(canvas,{src,cells,speed}) renders a turning
   globe as a screen-fixed dot grid: dot size follows the Earth map's brightness (clouds big,
   ocean small) and dot colour is a slowly flowing pink/violet/blue/cyan/orange gradient.
   On a light page it prints like ink (dark ocean = big dots, clouds = paper);
   on a dark page it glows (clouds = big dots). Pauses off screen and in hidden tabs; reduced motion draws one still frame. */
window.sgGlobe=(cv,o={})=>{
 const RM=matchMedia("(prefers-reduced-motion: reduce)"),gl=cv.getContext("webgl",{premultipliedAlpha:true,alpha:true,antialias:false});
 if(!gl){cv.classList.add("nogl");return}
 const FS=`precision highp float;uniform float t,cs,ink;uniform vec2 res;uniform sampler2D map;
const float PI=3.14159265;const float R=${(o.r||.86).toFixed(3)};
vec3 siri(vec2 p,float t){
 float a=atan(p.y,p.x)/(2.*PI)+.5;
 float f=fract(a+t*.045+.18*sin(t*.35+p.y*2.4)+.12*sin(t*.27+p.x*3.1));
 vec3 c0=vec3(1.,.33,.62),c1=vec3(.66,.36,1.),c2=vec3(.25,.52,1.),c3=vec3(.22,.85,1.),c4=vec3(1.,.58,.32);
 float x=f*5.;vec3 c=mix(c0,c1,smoothstep(0.,1.,x));
 c=mix(c,c2,smoothstep(1.,2.,x));c=mix(c,c3,smoothstep(2.,3.,x));c=mix(c,c4,smoothstep(3.,4.,x));c=mix(c,c0,smoothstep(4.,5.,x));
 return c;}
float lum(vec2 q){
 float r2=dot(q,q);if(r2>1.)return -1.;
 float z=sqrt(1.-r2);float tl=.38;
 vec3 s=vec3(q.x,q.y*cos(tl)+z*sin(tl),-q.y*sin(tl)+z*cos(tl));
 float lon=atan(s.x,s.z)+t*${(o.speed||.12).toFixed(3)},lat=asin(clamp(s.y,-1.,1.));
 float L=texture2D(map,vec2(fract(lon/(2.*PI)+.5),.5-lat/PI)).r;
 return clamp(mix(.07,1.,L)*(.5+.5*pow(z,.6)),0.,1.);}
void main(){
 vec2 fc=gl_FragCoord.xy,c=(floor(fc/cs)+.5)*cs;
 vec2 p=(c/res*2.-1.)/R,pf=(fc/res*2.-1.)/R;
 float L=lum(p);vec3 col=siri(pf,t);
 float a=0.;
 if(L>=0.){float v=mix(L,pow(1.-L*.97,1.7),ink),d=length(fc-c)/cs,rad=mix(.56,.5,ink)*sqrt(v)+.04;col=mix(col,col*col*.9,ink*.35);a=1.-smoothstep(rad-1.2/cs,rad,d);}
 float r=length(pf);
 float glow=smoothstep(1.09,1.,r)*smoothstep(.96,1.,r)*${(o.glow??.4).toFixed(3)};
 vec3 gc=siri(pf,t+2.);
 vec3 o=col*a+gc*glow*(1.-a);float A=a+glow*(1.-a);
 gl_FragColor=vec4(o,A);}`;
 const sh=(ty,s)=>{const x=gl.createShader(ty);gl.shaderSource(x,s);gl.compileShader(x);if(!gl.getShaderParameter(x,gl.COMPILE_STATUS))console.warn(gl.getShaderInfoLog(x));return x};
 const pr=gl.createProgram();gl.attachShader(pr,sh(gl.VERTEX_SHADER,"attribute vec2 a;void main(){gl_Position=vec4(a,0.,1.);}"));gl.attachShader(pr,sh(gl.FRAGMENT_SHADER,FS));gl.linkProgram(pr);
 if(!gl.getProgramParameter(pr,gl.LINK_STATUS)){cv.classList.add("nogl");return}
 gl.useProgram(pr);gl.bindBuffer(gl.ARRAY_BUFFER,gl.createBuffer());gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,1,1]),gl.STATIC_DRAW);
 const la=gl.getAttribLocation(pr,"a");gl.enableVertexAttribArray(la);gl.vertexAttribPointer(la,2,gl.FLOAT,false,0,0);
 const U={t:gl.getUniformLocation(pr,"t"),cs:gl.getUniformLocation(pr,"cs"),ink:gl.getUniformLocation(pr,"ink"),res:gl.getUniformLocation(pr,"res")};
 const tx=gl.createTexture();let ready=false,vis=true,raf=0,last=0;const T0=performance.now();
 const im=new Image();im.onload=()=>{gl.bindTexture(gl.TEXTURE_2D,tx);gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL,false);
  gl.texImage2D(gl.TEXTURE_2D,0,gl.LUMINANCE,gl.LUMINANCE,gl.UNSIGNED_BYTE,im);
  gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_MIN_FILTER,gl.LINEAR);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_MAG_FILTER,gl.LINEAR);
  gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_WRAP_S,gl.REPEAT);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_WRAP_T,gl.CLAMP_TO_EDGE);ready=true;size();kick()};
 im.src=o.src;
 function size(){const d=Math.min(2,devicePixelRatio||1),w=Math.max(1,Math.round(cv.clientWidth*d));if(cv.width!==w){cv.width=cv.height=w;gl.viewport(0,0,w,w)}
  gl.uniform2f(U.res,w,w);gl.uniform1f(U.cs,Math.max(Math.round(2.5*d),Math.round(w/(o.cells||96))))}
 function theme(){const m=getComputedStyle(cv).color.match(/[\d.]+/g);const k=m?(.3*m[0]+.59*m[1]+.11*m[2])/255:1;gl.uniform1f(U.ink,k<.5?1:0)}
 function draw(s){theme();gl.uniform1f(U.t,s);gl.clearColor(0,0,0,0);gl.clear(gl.COLOR_BUFFER_BIT);gl.drawArrays(gl.TRIANGLE_STRIP,0,4)}
 function loop(n){raf=0;if(!vis||document.hidden||RM.matches)return;if(n-last>32){last=n;draw((n-T0)/1000+4)}raf=requestAnimationFrame(loop)}
 function kick(){if(!ready)return;if(RM.matches){draw(4);return}if(!raf&&vis)raf=requestAnimationFrame(loop)}
 "IntersectionObserver"in window&&new IntersectionObserver(e=>{vis=e[0].isIntersecting;kick()}).observe(cv);
 "ResizeObserver"in window&&new ResizeObserver(()=>{if(ready){size();RM.matches&&draw(4)}}).observe(cv);
 document.addEventListener("visibilitychange",kick);RM.addEventListener&&RM.addEventListener("change",kick);
};
