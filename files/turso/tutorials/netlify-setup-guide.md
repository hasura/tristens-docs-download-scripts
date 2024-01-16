# Netlify setup guide

In this setup guide, you will deploy a web application that uses[ Turso ](https://turso.tech)as its
database. The deployment is configured with environment variables whose values
are obtained from the[ Turso CLI ](https://docs.turso.tech/reference/turso-cli).

You can find the[ source code for the app on GitHub ](https://github.com/turso-extended/app-find-me-on).

## Prerequisites​

- A[ Netlify account ](https://app.netlify.com/signup)
- The Turso CLI installed on your machine ([ installation instructions ](https://docs.turso.tech/reference/turso-cli#installation))


## 1. Set up the Turso database​

### 1a. Create a new database​

Run the following CLI command:

`$ turso db create findmeon`

### 1b. Access the database using the shell​

Run the following CLI command:

`$ turso db shell findmeon`

### 1c. Define and populate the database​

Copy and paste the following SQL statements into the shell to create tables,
indexes, and sample data:

```
-- users table
create   table  users (
  id  integer   primary   key ,
  email  varchar ( 255 )   not   null ,
  full_name  varchar ( 100 )   not   null ,
  username  varchar ( 50 )   not   null ,
  created_at  integer   default   ( cast ( unixepoch ( )   as   int ) )
) ;
-- links table
create   table  links (
  id  integer   primary   key ,
  user_id  integer   not   null ,
  website  varchar ( 100 )   not   null ,
  link  text   not   null ,
  created_at  integer   default   ( cast ( unixepoch ( )   as   int ) ) ,
   foreign   key ( user_id )   references  users ( id )
) ;
-- unique index for the email row
create   unique   index  idx_users_email  on  users ( email ) ;
-- unique index for the username row
create   unique   index  idx_users_username  on  users ( username ) ;
-- a multicolumn index for the user_id and link columns
create   unique   index  idx_links_userid_link  on  links ( user_id ,  link ) ;
-- create user: "turso"
insert   into  users ( id ,  email ,  full_name ,  username )   values ( 1 ,   "no-reply@turso.tech" ,   "Turso" ,   "turso" ) ;
-- add some links to "turso"
insert   into  links ( user_id ,  website ,  link )   values ( 1 ,   "Twitter" ,   "https://twitter.com/tursodatabase" ) ,
( 1 ,   "Linkedin" ,   "https://www.linkedin.com/company/turso/" ) ,
( 1 ,   "GitHub" ,   "https://github.com/chiselstrike/" ) ;
```

### 1d. Quit the shell​

Type the following at the shell prompt to terminate the shell:

`.quit`

## 2. Deploy the app to Netlify​

### 2a. Start a guided installation​

Click this button to start a guided deployment. It will automatically copy the[ app's source code ](https://github.com/turso-extended/app-find-me-on)into your personal GitHub and deploy it from there.

[  ](https://app.netlify.com/start/deploy?repository=https://github.com/turso-extended/app-find-me-on)

Image: [ Deploy to Netlify ](https://www.netlify.com/img/deploy/button.svg)

note

If you would prefer to fork and deploy the source repo and configure the
deployment manually, follow the[ manual installation instructions ](https://docs.turso.tech//tutorials/netlify-setup-guide/#manual-installation)at the end of
this page. The following instructions assume that you're using the above button
to perform the deployment.

### 2b. Connect your Netlify account to your GitHub account​

Netlify will prompt you to log in with your GitHub account:

Image: [ Screenshot of connecting Netlify to GitHub ](https://docs.turso.tech/assets/images/01-connect-netlify-github-a86781074b066ba1824f4f4c5e1f8916.png)

Image: [ Screenshot of connecting Netlify to GitHub ](https://docs.turso.tech/assets/images/01-connect-netlify-github-a86781074b066ba1824f4f4c5e1f8916.png)

### 2c. Provide values for the project's environment variables​

The app (FindMeOn) requires two environment variables to enable it to connect to
the database you created earlier: `VITE_TURSO_DB_URL` and `VITE_TURSO_DB_AUTH_TOKEN` . These values are required by the[ libSQL TypeScript
client SDK ](https://docs.turso.tech/reference/client-access/javascript-typescript-sdk)to initialize the client and connect to the Turso database.

Netlify prompts you for those values on the page you see after logging in.

#### Get the value for VITE_TURSO_DB_URL​

`VITE_TURSO_DB_URL`

Run the following CLI command:

`$ turso db show findmeon --url`

It outputs the URL for the database. Copy that string into the `VITE_TURSO_DB_URL` variable.

#### Get the value for VITE_TURSO_DB_AUTH_TOKEN​

`VITE_TURSO_DB_AUTH_TOKEN`

Run the following CLI command:

`$ turso db tokens create findmeon`

This creates a long-lived authentication token that allows the libSQL client
library used by the app to connect to the database.

Copy the string into the `VITE_TURSO_DB_AUTH_TOKEN` variable.

#### Deploy the app​

Click the "Save & Deploy" button to finalize the project’s deployment.

Image: [ Screenshot of Netlify prompting for environment variables ](https://docs.turso.tech/assets/images/02-netlify-prompt-env-vars-ea2114c35e6702626a87c00305094423.png)

Image: [ Screenshot of Netlify prompting for environment variables ](https://docs.turso.tech/assets/images/02-netlify-prompt-env-vars-ea2114c35e6702626a87c00305094423.png)

This will take you to the "Site overview" page on your Netlify dashboard which
displays the deployment status of the project. Once deployment is complete, you
can verify that the app works.

Image: [ Screenshot of Netlify deployment status ](https://docs.turso.tech/assets/images/03-netlify-deployment-status-805ab8ad1dc644a2ac9c5b31a5e6060d.png)

Image: [ Screenshot of Netlify deployment status ](https://docs.turso.tech/assets/images/03-netlify-deployment-status-805ab8ad1dc644a2ac9c5b31a5e6060d.png)

## 3. Verify the app works​

In step 1, you created and populated the database with some sample data. You can
use the deployed app to view the sample data to verify that it's correctly
connected to Turso.

Using the deployment URL provided by Netlify, visit the path `/u/turso` under
it. This page displays the user data from the `users` and `links` tables.

Image: [ Screenshot of deployed app working ](https://docs.turso.tech/assets/images/04-verify-app-works-68e88a8c6c2ed6da264d217f55a1492a.png)

Image: [ Screenshot of deployed app working ](https://docs.turso.tech/assets/images/04-verify-app-works-68e88a8c6c2ed6da264d217f55a1492a.png)

## (Alternative) manual installation​

If you want to deploy an app without the help of the "Deploy to Netlify" button
in step 2, you can instead use the Netlify dashboard to manually specify your
GitHub repo and configure its environment variables. The steps below walk you
through this process using the same source repository.

### 1. Fork the repo​

Visit the[ project on GitHub ](https://github.com/turso-extended/app-find-me-on)and fork the repository to your own personal
account.

### 2. Import the project in the Netlify dashboard​

Open your Netlify dashboard, add a new site, and import the existing project
that you just forked.

Image: [ Screenshot of importing a project in Netlify ](https://docs.turso.tech/assets/images/05-netlify-import-project-f67068f2d3442d7d4a1708e097dd2c92.png)

Image: [ Screenshot of importing a project in Netlify ](https://docs.turso.tech/assets/images/05-netlify-import-project-f67068f2d3442d7d4a1708e097dd2c92.png)

### 3. Connect to a Git provider​

Choose GitHub from the list (if you forked the repo in step 1).

Image: [ Screenshot of connecting a Git project in Netlify ](https://docs.turso.tech/assets/images/06-netlify-connect-git-provider-3e2edb2298f7455c01997012a5583634.png)

Image: [ Screenshot of connecting a Git project in Netlify ](https://docs.turso.tech/assets/images/06-netlify-connect-git-provider-3e2edb2298f7455c01997012a5583634.png)

### 4. Pick your project’s repository​

Netlify provides a list of repositories in your account. Choose your fork from
the list.

Image: [ Screenshot of picking a git project in Netlify ](https://docs.turso.tech/assets/images/07-netlify-pick-repository-647e258319efd908b678de9de92536c5.png)

Image: [ Screenshot of picking a git project in Netlify ](https://docs.turso.tech/assets/images/07-netlify-pick-repository-647e258319efd908b678de9de92536c5.png)

### 5. Configure site settings​

Configure the site settings for your project, including the production branch,
build command, publish and base directory. (For most frameworks, Netlify
automatically detects and sets this configuration.)

Image: [ Screenshot of configuring site settings in Netlify ](https://docs.turso.tech/assets/images/08-netlify-site-settings-dca1ab7d2c10a4f5f3524ca23f50c015.png)

Image: [ Screenshot of configuring site settings in Netlify ](https://docs.turso.tech/assets/images/08-netlify-site-settings-dca1ab7d2c10a4f5f3524ca23f50c015.png)

### 6. Configure the app's environment variables​

The app (FindMeOn) requires two environment variables to enable it to connect to
the database you created earlier: `VITE_TURSO_DB_URL` and `VITE_TURSO_DB_AUTH_TOKEN` . These values are required by the[ libSQL TypeScript
client SDK ](https://docs.turso.tech/reference/client-access/javascript-typescript-sdk)to initialize the client and connect to the Turso database.

Click the "Show advanced" button on the site setting page.

#### 6a. Create an environment variable for VITE_TURSO_DB_URL​

`VITE_TURSO_DB_URL`

Use the "New variable" button to create a new environment variable called `VITE_TURSO_DB_URL` .

Image: [ Screenshot of adding an environment variable in Netlify ](https://docs.turso.tech/assets/images/09-netlify-create-env-var-0f19753dcb92098405603c5e821e9d98.png)

Image: [ Screenshot of adding an environment variable in Netlify ](https://docs.turso.tech/assets/images/09-netlify-create-env-var-0f19753dcb92098405603c5e821e9d98.png)

Run the following CLI command:

`$ turso db show findmeon --url`

It outputs the URL for the database. Copy that string into the `VITE_TURSO_DB_URL` variable.

#### 6b. Create an environment variable for VITE_TURSO_DB_AUTH_TOKEN​

`VITE_TURSO_DB_AUTH_TOKEN`

Use the "New variable" button to create a new environment variable called `VITE_TURSO_DB_AUTH_TOKEN` .

Run the following CLI command:

`$ turso db tokens create findmeon -e none`

This creates a long-lived authentication token that allows the libSQL client
library used by the app to connect to the database. The `-e` flag in this
command is short for `--expiration` .

Copy the string into the `VITE_TURSO_DB_AUTH_TOKEN` variable.

### 7. Deploy the site​

Image: [ Screenshot of deploying a site in Netlify ](https://docs.turso.tech/assets/images/10-netlify-deploy-site-91862180358731faddb1674bfd3e3dd1.png)

Image: [ Screenshot of deploying a site in Netlify ](https://docs.turso.tech/assets/images/10-netlify-deploy-site-91862180358731faddb1674bfd3e3dd1.png)

### 8. Preview the site after deployment​

Image: [ Screenshot of opening a preview in Netlify ](https://docs.turso.tech/assets/images/11-netlify-open-preview-dd6691bca20ce00fe3e5a33335b353bd.png)

Image: [ Screenshot of opening a preview in Netlify ](https://docs.turso.tech/assets/images/11-netlify-open-preview-dd6691bca20ce00fe3e5a33335b353bd.png)

- [ Prerequisites ](https://docs.turso.tech//tutorials/netlify-setup-guide/#prerequisites)
- [ 1. Set up the Turso database ](https://docs.turso.tech//tutorials/netlify-setup-guide/#1-set-up-the-turso-database)
    - [ 1a. Create a new database ](https://docs.turso.tech//tutorials/netlify-setup-guide/#1a-create-a-new-database)
- [ 2. Deploy the app to Netlify ](https://docs.turso.tech//tutorials/netlify-setup-guide/#2-deploy-the-app-to-netlify)
    - [ 2a. Start a guided installation ](https://docs.turso.tech//tutorials/netlify-setup-guide/#2a-start-a-guided-installation)
- [ 3. Verify the app works ](https://docs.turso.tech//tutorials/netlify-setup-guide/#3-verify-the-app-works)
- [ (Alternative) manual installation ](https://docs.turso.tech//tutorials/netlify-setup-guide/#manual-installation)
    - [ 1. Fork the repo ](https://docs.turso.tech//tutorials/netlify-setup-guide/#1-fork-the-repo)


- [ 

Sign Up




 ](https://api.turso.tech/?webui=true&type=signup)
- [ 

Star Our Repo






 ](https://github.com/libsql/libsql)


Sign Up

Star Our Repo

- [ About ](https://turso.tech/about-us)
- [ Investors ](https://turso.tech/investors)
- [ Blog ](https://blog.turso.tech)


- [ Turso Discord ](https://discord.com/invite/4B5D7hYwub)
- [ libSQL Discord ](https://discord.gg/VzbXemj6Rg)
- [ Follow us on Twitter ](https://twitter.com/tursodatabase)
- [ Schedule a Zoom ](https://calendly.com/d/gt7-bfd-83n/meet-with-chiselstrike)


- [ Turso GitHub ](https://github.com/tursodatabase/)
- [ Turso extended GitHub ](https://github.com/turso-extended/)
- [ libSQL GitHub ](http://github.com/tursodatabase/libsql)


- [ Privacy Policy ](https://turso.tech/privacy-policy)
- [ Terms of Use ](https://turso.tech/terms-of-use)


Image: [ Turso logo ](https://docs.turso.tech/img/turso.svg)