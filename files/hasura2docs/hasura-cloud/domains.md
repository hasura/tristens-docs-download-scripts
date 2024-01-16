# Custom Domains

## Introduction​

In the `Domains` tab of your Project, you can see the default Hasura domain, and you have the possibility to add custom
domains.

## Adding a custom domain​

You can add a custom domain to your Hasura Cloud project by following the steps below.

### Step 1: Navigate to add a custom domain​

On the `Domains` tab, click on the `New Custom Domain` button.

Image: [ Add custom domain ](https://hasura.io/docs/assets/images/add-custom-domain-2fc1c6f96e1bdf4fb021f58eb2a1f785.png)

### Step 2: Add your custom domain​

Enter your custom domain and click the `Add` button.

Image: [ Choose custom domain ](https://hasura.io/docs/assets/images/choose-custom-domain-f823d085e7b60eaa7acd27648e99b4b2.png)

### Step 3: Add the record to your DNS​

After adding a custom domain, the following window will show up:

Image: [ DNS settings ](https://hasura.io/docs/assets/images/dns-settings-ff2f15470a1ba388447176b883a12706.png)

Add the default Hasura domain as a `CNAME` record to your DNS.

Note

If you're using[ Cloudflare ](https://www.cloudflare.com)as your DNS provider, do not enable the proxy (orange cloud)
until the certificate is generated. i.e. `Proxy status` should be `DNS only` . You can enable the proxy after SSL
certificate is generated.

Until this is done, the dashboard will show a notice that the DNS validation is pending.

Image: [ DNS validation pending ](https://hasura.io/docs/assets/images/dns-validation-pending-56694dd6b05de8ddb52535a9c2369aa6.png)

Note

Depending on your DNS provider, it might take up to 24 hours for the DNS record to be added.

## DNS validated​

Once the DNS is validated, the dashboard will update the status with the following notice:

Image: [ DNS validated ](https://hasura.io/docs/assets/images/dns-validated-6cd9f39c0fe6ad7c90567e641795b7cc.png)

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/hasura-cloud/domains/#introduction)
- [ Adding a custom domain ](https://hasura.io/docs/latest/hasura-cloud/domains/#adding-a-custom-domain)
    - [ Step 1: Navigate to add a custom domain ](https://hasura.io/docs/latest/hasura-cloud/domains/#step-1-navigate-to-add-a-custom-domain)

- [ Step 2: Add your custom domain ](https://hasura.io/docs/latest/hasura-cloud/domains/#step-2-add-your-custom-domain)

- [ Step 3: Add the record to your DNS ](https://hasura.io/docs/latest/hasura-cloud/domains/#step-3-add-the-record-to-your-dns)
- [ DNS validated ](https://hasura.io/docs/latest/hasura-cloud/domains/#dns-validated)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)