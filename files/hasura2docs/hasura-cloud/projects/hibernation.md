# Project Hibernation and Reactivation

## Introduction​

As part of our regular maintenance cycle, projects on the free tier that haven't seen any API request activity for the
past three months are hibernated after two notices to their owners. Here are some FAQs related to the process and
reactivation:

## Frequently Asked Questions​

### My Hasura Cloud project is hibernated. What does this mean?​

All the Metadata and project details are still preserved, but you won't be able to make any API calls to the instance
endpoint. However, if you want to keep using your project, you can reactivate it manually from your project's section to
continue using Hasura seamlessly.

### How will I know when any of my projects will be hibernated?​

After sixty days of inactivity, the project owner will receive the first email informing them about the hibernation of
the project in 30 days.

Fifteen days after that, at the 75-day mark, they will receive a reminder.

Finally, another fifteen days later, they will receive a confirmation email informing that the project has been
hibernated.

### How do I abort the hibernation process?​

The hibernation process starts when your project is inactive for 60 days. If you make any GraphQL requests to your
project's API you will be generating activity and aborting the process.

### How do I reactivate my hibernated project?​

If you are the **project owner** , clicking on the `Reactivate` button of your project's section will allow you to
reactivate the project.

Image: [ Hibernated project as seen by the project owner ](https://hasura.io/docs/assets/images/reactivation-owner-9442b5ad6992747cb7271129bc1c98e8.png)

If you are a **collaborator** , the project's section will ask you to contact the project owner to let them reactivate
the project.

Image: [ Hibernated project as seen by a collaborator ](https://hasura.io/docs/assets/images/reactivation-collaborator-f694df74dc0cc6c8183ed7a465ea51c4.png)

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/hasura-cloud/projects/hibernation/#introduction)
- [ Frequently Asked Questions ](https://hasura.io/docs/latest/hasura-cloud/projects/hibernation/#frequently-asked-questions)
    - [ My Hasura Cloud project is hibernated. What does this mean? ](https://hasura.io/docs/latest/hasura-cloud/projects/hibernation/#my-hasura-cloud-project-is-hibernated-what-does-this-mean)

- [ How will I know when any of my projects will be hibernated? ](https://hasura.io/docs/latest/hasura-cloud/projects/hibernation/#how-will-i-know-when-any-of-my-projects-will-be-hibernated)

- [ How do I abort the hibernation process? ](https://hasura.io/docs/latest/hasura-cloud/projects/hibernation/#how-do-i-abort-the-hibernation-process)

- [ How do I reactivate my hibernated project? ](https://hasura.io/docs/latest/hasura-cloud/projects/hibernation/#how-do-i-reactivate-my-hibernated-project)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)