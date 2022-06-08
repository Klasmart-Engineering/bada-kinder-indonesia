module.exports = [
  "strapi::errors",
  {
    name: "strapi::security",
    config: {
      contentSecurityPolicy: {
        useDefaults: true,
        directives: {
          "connect-src": ["'self'", "https:"],
          "img-src": [
            "'self'",
            "data:",
            "blob:",
            "klid-dev-bada-kinder.s3.ap-southeast-3.amazonaws.com",
            "klid-prod-bada-kinder.s3.ap-southeast-3.amazonaws.com",
          ],
          "media-src": [
            "'self'", 
            "data:", 
            "blob:", 
            "klid-dev-bada-kinder.s3.ap-southeast-3.amazonaws.com",
            "klid-prod-bada-kinder.s3.ap-southeast-3.amazonaws.com",
          ],
          upgradeInsecureRequests: null,
        },
      },
    },
  },
  'strapi::cors',
  'strapi::poweredBy',
  'strapi::logger',
  'strapi::query',
  'strapi::body',
  'strapi::session',
  'strapi::favicon',
  'strapi::public',
];
