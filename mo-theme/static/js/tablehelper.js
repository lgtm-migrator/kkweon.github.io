"use strict";

/**
 * Adds material design class table.
 */
function addMdlTableClass() {
  var tables = document.querySelectorAll("table");
  tables.forEach(function(table) {
    var className = "mdl-data-table mdl-js-data-table mdl-shadow--2dp";
    if (!table.className.includes(className)) {
      table.className += " " + className;
    }
  });
}

document.addEventListener("DOMContentLoaded", addMdlTableClass, false);
