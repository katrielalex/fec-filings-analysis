# donationsfrom.tech

This branch hosts https://donationsfrom.tech via Netlify's continuous integration.

To build, `make`, which reads `donations.yaml` and renders it through `template.jinja2`. This happens automatically when netlify deploys.

## Contributing

If you find some donations you think should be on here, please do make a pull request! Otherwise, you can send them to me via the contact form or by filing an issue, but it might take me a while to get around to them.

Instructions:

If the company logo is not in font-awesome:

  - find an SVG logo and add it to [logos.py](https://github.com/katrielalex/fec-filings-analysis/blob/gh-pages/logos.py). You'll probably need to twiddle with the bounding box and colors to make it look ok when rendered
  - add the company to the mapping at [the bottom of logos.py](https://github.com/katrielalex/fec-filings-analysis/blob/0aa82e9aeadee2c66b5067139b33a048858555e1/logos.py#L87)
  
Either way:
  - add the new donations to [donations.yaml](https://github.com/katrielalex/fec-filings-analysis/blob/gh-pages/donations.yaml)
