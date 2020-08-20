module.exports = {
	// The configuration settings for the OAS3 flow-node: ProdPad
	pluginConfig: {
		'@axway/api-builder-plugin-fn-swagger': {
			'prodpad-10': {}
		}
	},
	// The following authorization credentials needed to use this service.
	// Please follow this guide to manually configure these credentials:
	// https://docs.axway.com/bundle/API_Builder_4x_allOS_en/page/api_builder_credentials.html
	authorization: {
		credentials: {
			'ProdPad apiKey': {
				type: 'apiKey',
				key: process.env.PRODPAD_APIKEY
			}
		}
	}
};
