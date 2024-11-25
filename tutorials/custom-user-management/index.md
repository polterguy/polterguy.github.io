---
title: Creating a Custom User Management component
---

Every now and then you'll need to deliver something that allows for managing users and roles in the system and you can't use the Magic Dashboard for whatever reason. Luckily Magic contains all the backend API endpoints you'll ever need, assuming you're OK with only _"root"_ accounts being able to manage users. We _deeply encourage_ you to use these endpoints and _not_ create your own user system, since the existing RBAC-based user system permutates everything in Magic and already has existing slots and logic for all possible scenarios.

You will find the following API endpoints in Magic related to users.

* __POST - "/magic/system/magic/users"__ - Creates a new user
* __GET - "/magic/system/magic/users"__ - Returns a list of users matching an optional filtering criteria
* __PUT - "/magic/system/magic/users"__ - Updates an existing user
* __DELETE - "/magic/system/magic/users"__ - Deletes an existing user

## Creating and updating users

To create a new user you have to invoke the above POST endepoint. This endpoint takes a username and a password as JSON.

```json
{
  "username": "some_username",
  "password": "some_password"
}
```

This endpoint will hash the specified password using BlowFish with an individual seed, ensuring the password cannot be re-created from its hashed value using brute force or rainbow dictionary attacks. Notice, the above endpoint will throw an exception if the user already exists.

The PUT endpoint takes the exact same payload except it of course expects the user to already exist, and if it doesn't exist it will throw an exception. This endpoint basically only allows for changing a user's password, allowing for a root account to for instance reset a user's password.

Deleting a user works similarly, except it requires the username to be specified as a `username` QUERY parameter to its invocation.

## Retrieving users

To retrieve users from the backend you can use the above GET endpoint. Notice, this endpoint will also return all extra fields, in addition to the roles each user belongs to. In addition it allows for filtering, allowing you to search for users using a `username.eq` or `username.like` argument, in addition to query parameters for paging and ordering being `limit`, `offset`, `order` and `direction`. For instance, if you want to return users starting out with the characters _"fo"_ in their usernames ordered by username descending, and only return 5 results, you will need to use something resembling the following.

```text
/magic/system/magic/users?username.like=fo%25&order=username&direction=desc&limit=5
```

Notice, all endpoints that allows you to somehow modify users requires the username returned from the above invocation as its primary key to change the user. Also notice that Magic will never return the password of a user. However, finding the user's password is anyway cryptographically impossible, and if you've forgotten your password, it can only be reset, and not retrieved.

## Roles associations

Magic contains RBAC-based access control features, allowing you to restrict what users are allowed to access some resource by declaring what roles can access the resource. Then you associate one or more roles with each user. When you create a new user you typically want to associate it with one or more roles. The following endpoints allows for managing user's roles associations.

* __POST - "/magic/system/magic/users_roles"__ - Creates a new user/role association
* __GET - "/magic/system/magic/users_roles"__ - Returns a list of user/role associations matching an optional filtering criteria
* __DELETE - "/magic/system/magic/users_roles"__ - Deletes an existing user/role association

Notice, the above endpoints takes _"user"_ and _"role"_ as its arguments, and the GET and DELETE endpoints obviously takes these arguments as QUERY parameters - While the POST endpoint takes a JSON payload containing _"role"_ and _"user"_ fields. Below is an example of how to create a user/role association.

```json
{
  "role": "some_username",
  "user": "some_existing_role"
}
```

Notice, if the role or user doesn't exist, the above will of course throw an exception and return an error. Notice how the above does also not contain an update endpoint (PUT), since updating is effectively to delete one role association, for then to later create a new one. Also notice that the role you associate with a user must already exist or the backend will throw an exception.

## Managing roles

You can also manage roles using the following endpoints. Whether or not you want to do this, or use the existing Users and Roles component from Magic depends upon how much you want to do to abstract away Magic's dashboard. However, you _can_ create a custom role management component using Magic if you wish.

* __POST - "/magic/system/magic/roles"__ - Creates a new role
* __GET - "/magic/system/magic/roles"__ - Returns a list of roles matching an optional filtering criteria
* __PUT - "/magic/system/magic/roles"__ - Updates an existing role
* __DELETE - "/magic/system/magic/roles"__ - Deletes an existing role

A role has two basic fields; Name and description. When using PUT or POST from the above endpoints, you'll typically supply these as follows;

```json
{
  "name": "some_new_role",
  "description": "Description for your role"
}
```

When querying roles using the above GET endpoint you can filter using the following QUERY parameters.

* limit
* offset
* order
* direction
* name.eq
* name.like
* description.like

This is a general pattern in Magic, where each field typically has a bunch of comparison operators associated with it, such as illustrated above.

## Extra fields

Extra fields are additional information associated with the user. This can be name, email, address, etc. Anything really. The extra fields works similarly to the user/roles associations, and has the following endpoints.

* __POST - "/magic/system/magic/users_extra"__ - Creates a new extra field associated with an existing user
* __GET - "/magic/system/magic/users_extra"__ - Returns a list of extra fields matching an optional filtering criteria
* __PUT - "/magic/system/magic/users_extra"__ - Updates an existing extra field
* __DELETE - "/magic/system/magic/users_extra"__ - Deletes an existing extra field

Extra fields are divided by a _"type"_ field, which typically has a value such as _"email"_, _"name"_, or _"address"_, etc. To create a new extra field and associate with a user you can supply a payload such as the following to the above POST endpoint.

```json
{
  "type": "streetAddress",
  "value": "Foo Bar St. 57",
  "user": "some_existing_user"
}
```

The above will throw an exception if the user doesn't exist, and the type can only contain lowercase a to z, uppercase A-Z, 0 to 9, - or _ characters, and each user can only have one extra field of the same type - But the value can be anything you wish, and can be used to associate the user with additional extra information besides his or her username.

## Authorization

The really great thing about using these endpoints and the existing RBAC-based user module in Magic is that it ties into everything that already exists, allowing you to use the existing slots to authorize users before giving them access to some resource. Imagine the following Hyperlambda for instance.

```text
auth.ticket.verify:admin, marketing_manager, c_exec
```

The above Hyperlambda ensures that only users belonging to either of the following roles can access the code beneath it.

* admin
* marketing_manager
* c_exec

If any user not belonging to any of the above roles tries to execute the above code the system will throw an exception, preventing the rest of your Hyperlambda file to execute, resulting in an error being returned to the client.

## Wrapping up

This tutorial has shown you the basics of how to implement a user management component. If you want to play with these endpoints, or see every possible argument they can handle - You can use the [Endpoints component](https://docs.ainiro.io/dashboard/endpoints/) as your playground. Just make sure you check off _"System endpoints"_ to see internal endpoints.

![Managing users from the Endpoints component](/assets/images/endpoints-managing-users.png)

## Further reading

Magic also contains CCO/OIDC in addition to that it's also very easy to create your own registration endpoint. If you're interested in how to allow for users to register, you can [read the following article](https://ainiro.io/blog/create-a-registration-api-in-15-minutes).
