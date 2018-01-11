"use strict";

/**
 * Adds material design class table.
 */
function addTableClass() {
  var tables = document.querySelectorAll("table");
  tables.forEach(function(table) {
    table.classList.add("table");
  });
}

document.addEventListener("DOMContentLoaded", addTableClass, false);
