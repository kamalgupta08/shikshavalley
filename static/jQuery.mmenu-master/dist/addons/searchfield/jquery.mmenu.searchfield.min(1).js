/*	
 * jQuery mmenu searchfield addon
 * mmenu.frebsite.nl
 *
 * Copyright (c) Fred Heusschen
 */
!function(e){function s(e){switch(e){case 9:case 16:case 17:case 18:case 37:case 38:case 39:case 40:return!0}return!1}var n="mmenu",l="searchfield";e[n].addons[l]={setup:function(){var r=this,o=this.opts[l],c=this.conf[l];d=e[n].glbl,"boolean"==typeof o&&(o={add:o}),"object"!=typeof o&&(o={}),"boolean"==typeof o.resultsPanel&&(o.resultsPanel={add:o.resultsPanel}),o=this.opts[l]=e.extend(!0,{},e[n].defaults[l],o),c=this.conf[l]=e.extend(!0,{},e[n].configuration[l],c),this.bind("close",function(){this.$menu.find("."+a.search).find("input").blur()}),this.bind("init",function(n){if(o.add){var d;switch(o.addTo){case"panels":d=n;break;default:d=this.$menu.find(o.addTo)}if(d.each(function(){var s=e(this);if(!s.is("."+a.panel)||!s.is("."+a.vertical)){if(!s.children("."+a.search).length){var n=r.__valueOrFn(c.clear,s),l=r.__valueOrFn(c.form,s),t=r.__valueOrFn(c.input,s),d=r.__valueOrFn(c.submit,s),h=e("<"+(l?"form":"div")+' class="'+a.search+'" />'),u=e('<input placeholder="'+o.placeholder+'" type="text" autocomplete="off" />');h.append(u);var f;if(t)for(f in t)u.attr(f,t[f]);if(n&&e('<a class="'+a.btn+" "+a.clear+'" href="#" />').appendTo(h).on(i.click+"-searchfield",function(e){e.preventDefault(),u.val("").trigger(i.keyup+"-searchfield")}),l){for(f in l)h.attr(f,l[f]);d&&!n&&e('<a class="'+a.btn+" "+a.next+'" href="#" />').appendTo(h).on(i.click+"-searchfield",function(e){e.preventDefault(),h.submit()})}s.hasClass(a.search)?s.replaceWith(h):s.prepend(h).addClass(a.hassearch)}if(o.noResults){var p=s.closest("."+a.panel).length;if(p||(s=r.$pnls.children("."+a.panel).first()),!s.children("."+a.noresultsmsg).length){var v=s.children("."+a.listview).first();e('<div class="'+a.noresultsmsg+" "+a.hidden+'" />').append(o.noResults)[v.length?"insertAfter":"prependTo"](v.length?v:s)}}}}),o.search){if(o.resultsPanel.add){o.showSubPanels=!1;var h=this.$pnls.children("."+a.resultspanel);h.length||(h=e('<div class="'+a.panel+" "+a.resultspanel+" "+a.hidden+'" />').appendTo(this.$pnls).append('<div class="'+a.navbar+" "+a.hidden+'"><a class="'+a.title+'">'+o.resultsPanel.title+"</a></div>").append('<ul class="'+a.listview+'" />').append(this.$pnls.find("."+a.noresultsmsg).first().clone()),this.init(h))}this.$menu.find("."+a.search).each(function(){var n,d,c=e(this),u=c.closest("."+a.panel).length;u?(n=c.closest("."+a.panel),d=n):(n=e("."+a.panel,r.$menu),d=r.$menu),o.resultsPanel.add&&(n=n.not(h));var f=c.children("input"),p=r.__findAddBack(n,"."+a.listview).children("li"),v=p.filter("."+a.divider),m=r.__filterListItems(p),b="a",g=b+", span",C="",_=function(){var s=f.val().toLowerCase();if(s!=C){if(C=s,o.resultsPanel.add&&h.children("."+a.listview).empty(),n.scrollTop(0),m.add(v).addClass(a.hidden).find("."+a.fullsubopensearch).removeClass(a.fullsubopen+" "+a.fullsubopensearch),m.each(function(){var s=e(this),n=b;(o.showTextItems||o.showSubPanels&&s.find("."+a.next))&&(n=g);var l=s.data(t.searchtext)||s.children(n).text();l.toLowerCase().indexOf(C)>-1&&s.add(s.prevAll("."+a.divider).first()).removeClass(a.hidden)}),o.showSubPanels&&n.each(function(s){var n=e(this);r.__filterListItems(n.find("."+a.listview).children()).each(function(){var s=e(this),n=s.data(t.sub);s.removeClass(a.nosubresults),n&&n.find("."+a.listview).children().removeClass(a.hidden)})}),o.resultsPanel.add)if(""===C)this.closeAllPanels(),this.openPanel(this.$pnls.children("."+a.subopened).last());else{var l=e();n.each(function(){var s=r.__filterListItems(e(this).find("."+a.listview).children()).not("."+a.hidden).clone(!0);s.length&&(o.resultsPanel.dividers&&(l=l.add('<li class="'+a.divider+'">'+e(this).children("."+a.navbar).text()+"</li>")),l=l.add(s))}),l.find("."+a.next).remove(),h.children("."+a.listview).append(l),this.openPanel(h)}else e(n.get().reverse()).each(function(s){var n=e(this),l=n.data(t.parent);l&&(r.__filterListItems(n.find("."+a.listview).children()).length?(l.hasClass(a.hidden)&&l.children("."+a.next).not("."+a.fullsubopen).addClass(a.fullsubopen).addClass(a.fullsubopensearch),l.removeClass(a.hidden).removeClass(a.nosubresults).prevAll("."+a.divider).first().removeClass(a.hidden)):u||(n.hasClass(a.opened)&&setTimeout(function(){r.openPanel(l.closest("."+a.panel))},(s+1)*(1.5*r.conf.openingInterval)),l.addClass(a.nosubresults)))});d.find("."+a.noresultsmsg)[m.not("."+a.hidden).length?"addClass":"removeClass"](a.hidden),this.update()}};f.off(i.keyup+"-"+l+" "+i.change+"-"+l).on(i.keyup+"-"+l,function(e){s(e.keyCode)||_.call(r)}).on(i.change+"-"+l,function(e){_.call(r)});var w=c.children("."+a.btn);w.length&&f.on(i.keyup+"-"+l,function(e){w[f.val().length?"removeClass":"addClass"](a.hidden)}),f.trigger(i.keyup+"-"+l)})}}})},add:function(){a=e[n]._c,t=e[n]._d,i=e[n]._e,a.add("clear search hassearch resultspanel noresultsmsg noresults nosubresults fullsubopensearch"),t.add("searchtext"),i.add("change keyup")},clickAnchor:function(e,s){}},e[n].defaults[l]={add:!1,addTo:"panels",placeholder:"Search",noResults:"No results found.",resultsPanel:{add:!1,dividers:!0,title:"Search results"},search:!0,showTextItems:!1,showSubPanels:!0},e[n].configuration[l]={clear:!1,form:!1,input:!1,submit:!1};var a,t,i,d}(jQuery);