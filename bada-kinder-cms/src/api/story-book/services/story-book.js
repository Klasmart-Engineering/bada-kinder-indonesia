'use strict';

/**
 * story-book service.
 */

const { createCoreService } = require('@strapi/strapi').factories;

module.exports = createCoreService('api::story-book.story-book');
