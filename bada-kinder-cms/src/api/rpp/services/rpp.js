'use strict';

/**
 * rpp service.
 */

const { createCoreService } = require('@strapi/strapi').factories;

module.exports = createCoreService('api::rpp.rpp');
