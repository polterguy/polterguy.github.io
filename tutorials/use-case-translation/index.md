# Use case - Translating your app using Google Translate

Translating our apps is probably one of the most common problems we as software developers are asked
to do. This is a well known pattern, basically consisting of two simple database tables, allowing
our back office workers to do basic CRUD unto.
However, in this little use case, I will show you how you can almost *completely automate* this
process, by having Google Translate do the _"heavy lifting"_. First watch the following video.

<div style="position:relative; padding-bottom:56.25%; padding-top:30px; height:0; overflow:hidden;margin-top:4rem;margin-bottom:4rem;">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/2hrUi1o5rDg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

If you watch the above video, you will see how Google Translate automatically
translates my entities every time I insert an English item into my database.
90% of the time, this default translation is more than good enough. But even for the
cases where it's not, you can easily modify the item afterwards, by editing it using the
CRUD features of the generated frontend administrative dashboard Magic creates for you.
See a screenshot below for an example of the latter.

![Editing your translation entities](https://servergardens.files.wordpress.com/2020/10/editing-translation-entities.png)

Of course, the idea is that you give your translation back office workers direct access to the above dashboard,
such that they can themselves edit the entities that Google can't handle correctly for some reasons. This is
done easily by creating new users using the built in auth mechanisms of Magic. For the record, you do *not* want
to give these people root access. Probably smarter to create some new role, and associate your users with this role
instead. For then to make sure you give Create, Update and Delete rights to these roles during the crudifiction
process.

## Getting started

1. Make sure you have the latest version of Magic, at least version 8.4.1
2. Go to the SQL menu item, and choose the _"babelfish.sql"_ script, and execute it. Either in mysql or mssql-batch, depending upon which database you're using
3. Crudify your babelfish database, and make sure all of your `get` endpoints have *no* auth (authentication)
4. Generate your frontend

Then apply the following changes to the _"translations.post.hl"_ endpoint.

```
.arguments
   id:string
   locale:string
   content:string
.type:crud-create
auth.ticket.verify:root
mysql.connect:babelfish
   add:x:+/*/values
      get-nodes:x:@.arguments/*
   mysql.create
      table:translations
      return-id:bool:false
      values

   /*
    * This is where we duplicate our entry, but only if
    * the [locale] is English. Basically, we create a new
    * background thread, where we duplicate our entry, with
    * the results of invoking Google Translate for every
    * language we have in our database.
    */
   if
      eq
         get-value:x:@.arguments/*/locale
         .:en
      .lambda
         unwrap:x:./*/fork/*
         fork
            .text:x:@.arguments/*/content
            .id:x:@.arguments/*/id
            
            try
               mysql.connect:babelfish
                  mysql.read
                     table:languages
                     columns
                        locale
                     where
                        and
                           locale.neq:en
                  for-each:x:@mysql.read/*
                     unwrap:x:+/*
                     signal:magic.google.translate
                        text:x:@.text
                        src-lang:en
                        dest-lang:x:@.dp/#/*/locale
                     mysql.create
                        table:translations
                        values
                           id:x:@.id
                           locale:x:@.dp/#/*/locale
                           content:x:@signal
            .catch
               log.info:x:@.message


   // Continuing main thread
   unwrap:x:+/*
   return
      id:x:@mysql.create
```

This ensures that every time you save an English entity, Magic will translate your entity into
every single language you have declared in your _"languages"_ database table. Notice, you might
want to add up the language for all languages you intend to support *before* starting to add
entities into your database.

Then open your _"languages.component.ts"_ file in your frontend, and exchange its `displayedColumns` with the following.

```typescript
  public displayedColumns: string[] = [
    'description',
    'locale',
    'delete-instance'
  ];
```

Do the same in _"translations.comonent.ts"_, but use the following code.

```typescript
  public displayedColumns: string[] = [
    'id',
    'locale',
    'content',
    'delete-instance'
  ];
```

The above two code snippets just ensures your frontend displays the primary keys for
your database tables in your front end Material Table. Then modify your existing
`mat-form-field` for your `locale` in your _"edit.translations.component.html"_ file,
and exchange it with the following code.

```html
  <app-selector
    key="locale"
    value="description"
    [model]="data.entity"
    [getItems]="service.languages.read({limit: -1})"
    class="entity-edit-field">
  </app-selector>
```

The above code exchanges your (default) textbox with a dropdown select list, resembling the following.

![Choosing language](https://servergardens.files.wordpress.com/2020/10/choosing-language.png)

And you're done! You now have an _"automagic translation app"_, exposing two HTTP REST endpoints,
allowing you to easily translate all your apps into any language you wish - Including all 250
languages you don't know - Assuming Google knows them ofc ... ;)

* [Retrieve languages from localhost](http://localhost:55247/magic/modules/babelfish/languages?limit=-1)
* [Retrieve translations from localhost](http://localhost:55247/magic/modules/babelfish/translations?limit=-1&locale.eq=en)

Of course, as you deploy it into production, you'll [need a license key](https://servergardens.com/buy/), in addition
to that you'll need to exchange the root domain to something else but localhost. Then the idea is that you retrieve *only*
the language entities according to what language the user selects in your little app, adding the `locale.eq` parts
in the above HTTP request dynamically, matching the locale he or she selects as their primary language.

At which point you can dynamic substitute the entities in your frontend, according to a lookup into the result
returned from the _"translations"_ endpoint above.

# Wrapping up

If you want to be a little bit advanced, you might want to create *one additional* HTTP endpoint for retrieving
the contents of both your tables, where you apply some HTTP Cache-Control, in addition to some server side
caching. If you [buy a license](https://servergardens.com/buy/), and [ask me nicely](mailto:thomas@servergardens.com),
maybe I'll send you some code illustrating how to do this. This of course, makes your HTTP GET endpoints a gazillion
times faster, by applying *both* server side caching, in addition to a `Cache-Control` HTTP header as your endpoint
is invoked, making everything blistering fast, using literally *zero* server side resources. Hint, *don't cache too long*.
5 minutes should be more than enough.

* [Documentation](/documentation/)
