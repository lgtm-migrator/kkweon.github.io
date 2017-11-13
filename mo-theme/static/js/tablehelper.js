"use strict";

/**
 * Adds material design class table.
 */
function addMdlTableClass() {
  var tables = document.querySelectorAll("table");
  tables.forEach(function(table) {
    var className = "table table-responsive";
    if (!table.className.includes(className)) {
      table.className += " " + className;
    }
  });
}

document.addEventListener("DOMContentLoaded", addMdlTableClass, false);
