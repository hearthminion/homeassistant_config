(function(){"use strict";function a(){const b=d(["\n      .content {\n        display: flex;\n        flex-direction: column;\n        align-items: center;\n        justify-content: center;\n        width: 100%;\n        height: 100%;\n      }\n    "]);return a=function(){return b},b}function b(){const a=d(["\n      <div class=\"content\" @click="," \n        style=\"","\">\n        ","\n      </div>\n    "]);return b=function(){return a},a}function c(){const a=d([""]);return c=function(){return a},a}function d(a,b){return b||(b=a.slice(0)),Object.freeze(Object.defineProperties(a,{raw:{value:Object.freeze(b)}}))}function e(a){for(var b=1;b<arguments.length;b++){var c=null==arguments[b]?{}:arguments[b],d=Object.keys(c);"function"==typeof Object.getOwnPropertySymbols&&(d=d.concat(Object.getOwnPropertySymbols(c).filter(function(a){return Object.getOwnPropertyDescriptor(c,a).enumerable}))),d.forEach(function(b){f(a,b,c[b])})}return a}function f(a,b,c){return b in a?Object.defineProperty(a,b,{value:c,enumerable:!0,configurable:!0,writable:!0}):a[b]=c,a}(function(a,b){"object"==typeof exports&&"undefined"!=typeof module?b():"function"==typeof define&&define.amd?define(b):b()})(this,function(){class d{static get LitElement(){return Object.getPrototypeOf(customElements.get("home-assistant-main"))}static get LitHtml(){return this.LitElement.prototype.html}static get LitCSS(){return this.LitElement.prototype.css}static callService(a,b,c,d,f){a.callService(b,c,e({entity_id:d},f))}static toggleEntity(a,b){const c=f.includes(a.states[b].state);return d.turnOnOffEntity(a,b,c)}static turnOnOffEntity(a,b){let c=!(2<arguments.length&&void 0!==arguments[2])||arguments[2];const e=d.computeDomain(b),f="group"===e?"homeassistant":e;let g;return g="lock"===e?c?"unlock":"lock":"cover"===e?c?"open_cover":"close_cover":c?"turn_on":"turn_off",a.callService(f,g,{entity_id:b})}static computeDomain(a){return a.substr(0,a.indexOf("."))}static popUp(a,b,c){let d=!!(3<arguments.length&&void 0!==arguments[3])&&arguments[3],e=document.createElement("div");e.innerHTML="\n      <style>\n        app-toolbar {\n          color: var(--more-info-header-color);\n          background-color: var(--more-info-header-background);\n        }\n      </style>\n      <app-toolbar>\n        <paper-icon-button\n          icon=\"hass:close\"\n          dialog-dismiss=\"\"\n        ></paper-icon-button>\n        <div class=\"main-title\" main-title=\"\">\n          ".concat(b,"\n        </div>\n      </app-toolbar>\n    "),e.appendChild(c),this.moreInfo(Object.keys(a.states)[0]);let f=document.querySelector("home-assistant")._moreInfoEl;return f._page="none",f.shadowRoot.appendChild(e),f.style.width="570px",document.querySelector("home-assistant").provideHass(c),setTimeout(()=>{let a=setInterval(()=>{f.getAttribute("aria-hidden")&&(e.parentNode.removeChild(e),clearInterval(a))},100)},1e3),f}static closePopUp(){let a=document.querySelector("home-assistant")._moreInfoEl;a&&a.close()}static moreInfo(a){this.fireEvent("hass-more-info",{entityId:a})}static fireEvent(a,b){let c=2<arguments.length&&void 0!==arguments[2]?arguments[2]:null;if(a=new Event(a,{bubbles:!0,cancelable:!1,composed:!0}),a.detail=b||{},c)c.dispatchEvent(a);else{var d=document.querySelector("home-assistant");d=d&&d.shadowRoot,d=d&&d.querySelector("home-assistant-main"),d=d&&d.shadowRoot,d=d&&d.querySelector("app-drawer-layout partial-panel-resolver"),d=d&&d.shadowRoot||d,d=d&&d.querySelector("ha-panel-lovelace"),d=d&&d.shadowRoot,d=d&&d.querySelector("hui-root"),d=d&&d.shadowRoot,d=d&&d.querySelector("ha-app-layout #view"),d=d&&d.firstElementChild,d&&d.dispatchEvent(a)}}static navigate(a,b,c){c?history.replaceState(null,"",b):history.pushState(null,"",b),fireEvent(window,"location-changed",{replace:c})}}const f=["closed","locked","off"];var g=function(a,b,c,e){var f;switch(e&&c.hold_action?f=c.hold_action:!e&&c.tap_action&&(f=c.tap_action),f||(f={action:"more-info"}),f.action){case"more-info":(c.entity||c.camera_image)&&d.fireEvent(a,"hass-more-info",{entityId:c.entity?c.entity:c.camera_image});break;case"navigate":f.navigation_path&&d.navigate(a,f.navigation_path);break;case"toggle":c.entity&&d.toggleEntity(b,c.entity);break;case"call-service":{if(!f.service)return;var g=f.service.split(".",2),h=g[0],i=g[1];b.callService(h,i,f.service_data)}}};class h extends d.LitElement{constructor(){super(),this._config={}}static get properties(){return{hass:{},config:{}}}setConfig(a){if(!a.text)throw Error("Invalid Configuration: 'text' required");this._config=a}render(){if(!this._config||!this.hass||!this._config.text)return d.LitHtml(c());const a=this.hass&&this._config.entity?this.hass.states[this._config.entity]:void 0;let e="";this._config.tap_action&&(e="cursor: pointer;");const f=a?a.state:"unavailable";return this._config.state_filter&&this._config.state_filter[f]&&(e+=this._config.state_filter[f]),d.LitHtml(b(),this._handleTap,e,this._config.text)}static get styles(){return d.LitCSS(a())}_handleTap(){this._config.tap_action&&g(this,this.hass,this._config,!1)}}customElements.define("text-action-element",h)})})();
