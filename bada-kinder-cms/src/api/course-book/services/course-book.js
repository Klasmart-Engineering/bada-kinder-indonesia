'use strict';

/**
 * course-book service.
 */

const { createCoreService } = require('@strapi/strapi').factories;

module.exports = createCoreService('api::course-book.course-book');
