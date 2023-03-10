/*	
 * jQuery mmenu navbar addon
 * mmenu.frebsite.nl
 *
 * Copyright (c) Fred Heusschen
 */
!function(n){var a="mmenu",t="navbars";n[a].addons[t]={setup:function(){var r=this,s=this.opts[t],c=this.conf[t];if(i=n[a].glbl,"undefined"!=typeof s){s instanceof Array||(s=[s]);var o={};n.each(s,function(i){var d=s[i];"boolean"==typeof d&&d&&(d={}),"object"!=typeof d&&(d={}),"undefined"==typeof d.content&&(d.content=["prev","title"]),d.content instanceof Array||(d.content=[d.content]),d=n.extend(!0,{},r.opts.navbar,d);var l=d.position,h=d.height;"number"!=typeof h&&(h=1),h=Math.min(4,Math.max(1,h)),"bottom"!=l&&(l="top"),o[l]||(o[l]=0),o[l]++;var f=n("<div />").addClass(e.navbar+" "+e.navbar+"-"+l+" "+e.navbar+"-"+l+"-"+o[l]+" "+e.navbar+"-size-"+h);o[l]+=h-1;for(var u=0,v=0,p=d.content.length;v<p;v++){var b=n[a].addons[t][d.content[v]]||!1;b?u+=b.call(r,f,d,c):(b=d.content[v],b instanceof n||(b=n(d.content[v])),f.append(b))}u+=Math.ceil(f.children().not("."+e.btn).length/h),u>1&&f.addClass(e.navbar+"-content-"+u),f.children("."+e.btn).length&&f.addClass(e.hasbtns),f.prependTo(r.$menu)});for(var d in o)r.$menu.addClass(e.hasnavbar+"-"+d+"-"+o[d])}},add:function(){e=n[a]._c,r=n[a]._d,s=n[a]._e,e.add("close hasbtns")},clickAnchor:function(n,a){}},n[a].configuration[t]={breadcrumbSeparator:"/"},n[a].configuration.classNames[t]={};var e,r,s,i}(jQuery),/*	
 * jQuery mmenu navbar addon breadcrumbs content
 * mmenu.frebsite.nl
 *
 * Copyright (c) Fred Heusschen
 */
function(n){var a="mmenu",t="navbars",e="breadcrumbs";n[a].addons[t][e]=function(t,e,r){var s=n[a]._c,i=n[a]._d;s.add("breadcrumbs separator");var c=n('<span class="'+s.breadcrumbs+'" />').appendTo(t);this.bind("init",function(a){a.removeClass(s.hasnavbar).each(function(){for(var a=[],t=n(this),e=n('<span class="'+s.breadcrumbs+'"></span>'),c=n(this).children().first(),o=!0;c&&c.length;){c.is("."+s.panel)||(c=c.closest("."+s.panel));var d=c.children("."+s.navbar).children("."+s.title).text();a.unshift(o?"<span>"+d+"</span>":'<a href="#'+c.attr("id")+'">'+d+"</a>"),o=!1,c=c.data(i.parent)}e.append(a.join('<span class="'+s.separator+'">'+r.breadcrumbSeparator+"</span>")).appendTo(t.children("."+s.navbar))})});var o=function(){c.html(this.$pnls.children("."+s.current).children("."+s.navbar).children("."+s.breadcrumbs).html())};return this.bind("openPanel",o),this.bind("init",o),0}}(jQuery),/*	
 * jQuery mmenu navbar addon close content
 * mmenu.frebsite.nl
 *
 * Copyright (c) Fred Heusschen
 */
function(n){var a="mmenu",t="navbars",e="close";n[a].addons[t][e]=function(t,e){var r=n[a]._c,s=n[a].glbl,i=n('<a class="'+r.close+" "+r.btn+'" href="#" />').appendTo(t),c=function(n){i.attr("href","#"+n.attr("id"))};return c.call(this,s.$page),this.bind("setPage",c),-1}}(jQuery),/*	
 * jQuery mmenu navbar addon next content
 * mmenu.frebsite.nl
 *
 * Copyright (c) Fred Heusschen
 */
function(n){var a="mmenu",t="navbars",e="next";n[a].addons[t][e]=function(e,r){var s,i,c=n[a]._c,o=n('<a class="'+c.next+" "+c.btn+'" href="#" />').appendTo(e),d=function(n){n=n||this.$pnls.children("."+c.current);var a=n.find("."+this.conf.classNames[t].panelNext);s=a.attr("href"),i=a.html(),o[s?"attr":"removeAttr"]("href",s),o[s||i?"removeClass":"addClass"](c.hidden),o.html(i)};return this.bind("openPanel",d),this.bind("init",function(){d.call(this)}),-1},n[a].configuration.classNames[t].panelNext="Next"}(jQuery),/*	
 * jQuery mmenu navbar addon prev content
 * mmenu.frebsite.nl
 *
 * Copyright (c) Fred Heusschen
 */
function(n){var a="mmenu",t="navbars",e="prev";n[a].addons[t][e]=function(e,r){var s=n[a]._c,i=n('<a class="'+s.prev+" "+s.btn+'" href="#" />').appendTo(e);this.bind("init",function(n){n.removeClass(s.hasnavbar).children("."+s.navbar).addClass(s.hidden)});var c,o,d=function(n){if(n=n||this.$pnls.children("."+s.current),!n.hasClass(s.vertical)){var a=n.find("."+this.conf.classNames[t].panelPrev);a.length||(a=n.children("."+s.navbar).children("."+s.prev)),c=a.attr("href"),o=a.html(),i[c?"attr":"removeAttr"]("href",c),i[c||o?"removeClass":"addClass"](s.hidden),i.html(o)}};return this.bind("openPanel",d),this.bind("init",function(){d.call(this)}),-1},n[a].configuration.classNames[t].panelPrev="Prev"}(jQuery),/*	
 * jQuery mmenu navbar addon searchfield content
 * mmenu.frebsite.nl
 *
 * Copyright (c) Fred Heusschen
 */
function(n){var a="mmenu",t="navbars",e="searchfield";n[a].addons[t][e]=function(t,e){var r=n[a]._c,s=n('<div class="'+r.search+'" />').appendTo(t);return"object"!=typeof this.opts.searchfield&&(this.opts.searchfield={}),this.opts.searchfield.add=!0,this.opts.searchfield.addTo=s,0}}(jQuery),/*	
 * jQuery mmenu navbar addon title content
 * mmenu.frebsite.nl
 *
 * Copyright (c) Fred Heusschen
 */
function(n){var a="mmenu",t="navbars",e="title";n[a].addons[t][e]=function(e,r){var s,i,c=n[a]._c,o=n('<a class="'+c.title+'" />').appendTo(e),d=function(n){if(n=n||this.$pnls.children("."+c.current),!n.hasClass(c.vertical)){var a=n.find("."+this.conf.classNames[t].panelTitle);a.length||(a=n.children("."+c.navbar).children("."+c.title)),s=a.attr("href"),i=a.html()||r.title,o[s?"attr":"removeAttr"]("href",s),o[s||i?"removeClass":"addClass"](c.hidden),o.html(i)}};return this.bind("openPanel",d),this.bind("init",function(n){d.call(this)}),0},n[a].configuration.classNames[t].panelTitle="Title"}(jQuery);