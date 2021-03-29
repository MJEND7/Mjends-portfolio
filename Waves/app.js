gsap.registerPlugin(ScrollTrigger);
gsap.set(".banner3d-1", { perspectiveOrigin: "center -100vh"});
gsap.set(".banner3d-2", { perspectiveOrigin: "center -100vh"});
gsap.set(".banner3d-3", { perspectiveOrigin: "center -100vh"});
gsap.set(".banner3d-4", { perspectiveOrigin: "left -100vh"});

gsap.to(".banner3d-1", {
  scrollTrigger: {
    trigger: ".banner3d-1",
    scrub: true,
    start: "top bottom",
    end: "bottom top"
  },
  perspectiveOrigin: "center 100vh", 
  ease: "none"
});

gsap.to(".banner3d-2", {
  scrollTrigger: {
    trigger: ".banner3d-2",
    scrub: true,
    start: "top bottom",
    end: "bottom top"
  },
  perspectiveOrigin: "center 100vh", 
  ease: "none"
});

gsap.to(".banner3d-3", {
  scrollTrigger: {
    trigger: ".banner3d-3",
    scrub: true,
    start: "top bottom",
    end: "bottom top"
  },
  perspectiveOrigin: "center 100vh", 
  ease: "none"
});

gsap.to(".banner3d-4", {
  scrollTrigger: {
    trigger: ".banner3d-4",
    scrub: true,
    start: "top bottom",
    end: "bottom top"
  },
  perspectiveOrigin: "left 100vh", 
  ease: "none"
});
  
