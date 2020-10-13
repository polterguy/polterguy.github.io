# Theming and creating your own template

Out of the box Magic contains several _"themes"_. These are internally referred
to as _"templates"_, since they are scaffolders building different types of results.
Some of these templates generates pure Angular HTTP CRUD services for you, others
produce a fully fledged GUI for you. However, you can also create your own template
if you wish, including templates creating React projects. Below is a screenshot of
the _"angular-dark"_ template.

![The Angular Dark template](https://servergardens.files.wordpress.com/2020/10/magic-dark-theme.png)

If you prefer to watch a video of me demonstrating the process, and explaining the
template engine, you can watch the following video.

<div style="position:relative; padding-bottom:56.25%; padding-top:30px; height:0; overflow:hidden;margin-top:4rem;margin-bottom:4rem;">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/SjjK5deSD38" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

Once you understand the templating engine, you can easily create your own templates.
This might be something you want to do because you want to make sure all scaffolded
results comes out of the box with a similar UI, or because you want to create some
sort of dev factory, where your users can select from a pre-defined list of looks,
feels, and additional helper components - Producing the exact result your customer
wants. This is an attempt of explaining the templating engine, with the intent of
making you capable of creating your own custom templates.

## The templating process

When you click the _"Endpoints"_ menu item in your Magic Dashboard, what Magic
does, is to dynamically retrieve all folders inside of your _"/misc/templates/"_
folder, excluding the _"/common/"_ folder, assuming the rest of your folders
inside of here is a _"template engine"_, producing some sort of result.
Each template inside of this folder requires at the very least _two_ files.

* README.md - Being some description of your template in Markdown format
* generate.hl - Being the entry point for your template engine

To start out with creating your own template, the easiest is probably to
simply copy one of the existing template folders, such as the _"angular-dark"_
folder, give your template a name, and apply your changes incrementally,
testing out your changes as you modify your template.
By default, simply copying an existing template, giving it a new name (new folder name),
should immediately have your template working out of the box, since all paths
are assumed to be relative.

Each template have varying complexity, depending upon what it does. For instance,
the _"angular-service"_ template is much simpler than most of the other templates,
because it doesn't need to create GUI Angular components, router links, a navbar, etc as
it produces its end result. Others are highly complex in nature, such as the
_"angular-dark"_ and the _"angular-default"_ templates, because they need to
dynamically create router links, Angular components, modify your Angular module,
etc, etc, etc. And of course, how the end product ends up looking like after
the template engine has done its Magic, is also highly dependent upon your
database structure, how you scaffolded your tables, and what endpoints you
included as you generated your frontend.

## Creating an Angular UI template

You can have the scaffolder produce _any_ type of result you wish, including
React templates, ObjectiveC code, Java/Android code, etc - But here I will focus on
the main Angular templates called _"angular-dark"_ and _"angular-default"_.
The reason is because if you understand these two templates, which are highly
similar in nature, you can easily apply your knowledge into _any_ template
engine you wish. Hence, the process is as follows.

1. Structuring endpoints
2. Create HTTP service methods
3. Load all files in the _"templates/main/"_ folder recursively
4. Load all files in the _"templates/components/"_ folder recursively
5. Preprocessing folder names, making sure all files ends up at the root of the resulting ZIP file
6. Performing dynamic substitutions, and creating one component for each CRUD method group
7. Returning a ZIP file to the caller

The basic idea is that each CRUD endpoint method group, resulting from the
first point above, will generate one _"component"_ each. The name of this
component is dynamically created according to the name of your CRUD method group,
which again normally is determined according to the name of your database table.

Hence, the _"template/components/"_ folder will be duplicated once for each
CRUD method group in your backend, and dynamically modified according to
input/output of your HTTP REST methods, and then referenced inside of your
_"app.module.ts"_ file, and your _"router-declarations.ts"_ file, etc.

The most important parts above to understand, is probably the structure
of the structuring process of your endpoints. This is done by a shared
Hyperlambda file, found in _"common/structure-endpoints.hl"_, and it will
produce a result resembling the following for you.

```
.
   url:magic/modules/sakila/actor
   component-selector:app-actor
   component-name:ActorComponent
   component-filename:actor.component
   component-folder:actor
   component-header:Actor
   component-edit-name:EditActorComponent
   component-edit-filename:edit.actor.component
   component-routing-url:actor
   count-method:actor.count
   verbs
      delete
         service-method-name:actor.delete
         input
            actor_id:long
         output
         auth
            .:root
      get
         service-method-name:actor.read
         input
            limit:long
            offset:long
            order:string
            direction:string
            actor_id.mt:long
            actor_id.lt:long
            actor_id.mteq:long
            actor_id.lteq:long
            actor_id.neq:long
            actor_id.eq:long
            first_name.like:string
            first_name.mt:string
            first_name.lt:string
            first_name.mteq:string
            first_name.lteq:string
            first_name.neq:string
            first_name.eq:string
            last_name.like:string
            last_name.mt:string
            last_name.lt:string
            last_name.mteq:string
            last_name.lteq:string
            last_name.neq:string
            last_name.eq:string
            last_update.mt:date
            last_update.lt:date
            last_update.mteq:date
            last_update.lteq:date
            last_update.neq:date
            last_update.eq:date
         output
            actor_id:long
            first_name:string
            last_name:string
            last_update:date
         auth
            .:root
      post
         service-method-name:actor.create
         input
            first_name:string
            last_name:string
         output
         auth
            .:root
      put
         service-method-name:actor.update
         input
            actor_id:long
            first_name:string
            last_name:string
         output
         auth
            .:root
```

Above you can see how the process has clearly been able to _"group"_
related CRUD endpoints, and create fairly good URL suggestions,
component name suggestions, filename suggestions, etc for you. In addition,
it has determined the authentication required to invoke all endpoints,
each endpoint's input arguments, its resulting output, etc.
This process will generate one item for each CRUD endpoint method group such
as illustrated above.

This again gives you substitution values, you can dynamically substitute
with template arguments inside of your actual TypeScript, HTML and CSS files.
You can find these substitutions by looking at for instance
the _"templates/component/component.ts"_ file. It should resemble the
following. Notice the **[[xxx]]** parts, which are dynamically substituted
during the scaffolding process, according to the values/variable names found
during the above structuring process.

```typescript
import { Component, OnInit, ViewChild } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { GridComponent } from '../../base/grid.component';
import { MatPaginator } from '@angular/material';
import { MatDialog } from '@angular/material';
import { FormControl } from '@angular/forms';

import { Edit[[component-name]] } from './modals/edit.[[component-filename]]';
import { HttpService } from 'src/app/services/http-service';
import { AuthService } from 'src/app/services/auth-service';

/**
 * "Datagrid" component for displaying instance of [[component-header]]
 * entities from your HTTP REST backend.
 */
@Component({
  selector: '[[component-selector]]',
  templateUrl: './[[component-filename]].html',
  styleUrls: ['./[[component-filename]].scss']
})
export class [[component-name]] extends GridComponent implements OnInit {

  /**
   * Which columns we should display. Reorder to prioritize columns differently.
   * Notice! 'delete-instance' should always come last.
   */
  public displayedColumns: string[] = [
    [[displayed-columns]]
  ];

  // Need to view paginator as a child to update page index of it.
  @ViewChild(MatPaginator, {static: true}) paginator: MatPaginator;

  // Form control declarations to bind up with reactive form elements.
[[form-control-declarations]]
  // Constructor taking a bunch of services/helpers through dependency injection.
  constructor(
    protected authService: AuthService,
    protected snackBar: MatSnackBar,
    private httpService: HttpService,
    private dialog: MatDialog) {
      super(authService, snackBar);
  }

  /**
   * Overridde abstract method necessary to return the URL endpoint
   * for CRUD methods to base class.
   */
  protected url() {
    return '[[endpoint-url]]';
  }

  /**
   * Overridden abstract method from base class, that returns the Observable
   * necessary to actually retrieve items from backend.
   */
  protected read(filter: any) {
    return this.httpService.[[service-get-method]](filter);
  }

  /**
   * Overridden abstract method from base class, that returns the Observable
   * necessary to actually retrieve count of items from backend.
   */
  protected count(filter: any) {
    return this.httpService.[[service-count-method]](filter);
  }

  /**
   * Overridden abstract method from base class, that returns the Observable
   * necessary to actually delete items in backend.
   */
  protected delete(ids: any) {
    return this.httpService.[[service-delete-method]](ids);
  }

  /**
   * Implementation of abstract base class method, to reset paginator
   * of component.
   */
  protected resetPaginator() {
    this.paginator.pageIndex = 0;
    this.filter.offset = 0;
  }

  /**
   * OnInit implementation. Retrieves initial data (unfiltered),
   * and instantiates our FormControls.
   */
  public ngOnInit() {

    // Retrieves data from our backend, unfiltered, and binds our mat-table accordingly.
    this.getData();

    /*
     * Creating our filtering FormControl instances, which gives us "live filtering"
     * on our columns.
     */
[[form-control-instantiations]]  }

  /**
   * Invoked when user wants to edit an entity
   * 
   * This will show a modal dialog, allowing the user to edit his record.
   */
  public editEntity(entity: any) {

    const dialogRef = this.dialog.open(Edit[[component-name]], {
      data: this.getEditData(entity)
    });
    dialogRef.afterClosed().subscribe(res => {
      if (res) {
        this.setEditData(res, entity);
      }
    });
  }

  /**
   * Invoked when user wants to create a new entity
   * 
   * This will show a modal dialog, allowing the user to supply
   * the initial data for the entity.
   */
  public createEntity() {

    const dialogRef = this.dialog.open(Edit[[component-name]], {
      data: {
        isEdit: false,
        entity: {},
      }});
    dialogRef.afterClosed().subscribe((res: any) => {
      if (res) {
        this.itemCreated(res);
      }
    });
  }
}
```

Notice, the above is _not_ valid TypeScript, since it contains syntax errors,
due to that parts of the file is dynamically substituted during the scaffolding
process. However, the above `[[form-control-instantiations]]` for instance,
will be dynamically substituted with `FormControl` instantiations during
the scaffolding, resulting in something resembling the following.

```typescript
    /*
     * Creating our filtering FormControl instances, which gives us "live filtering"
     * on our columns.
     */
    this.actor_id = this.createFormControl('actor_id.eq');
    this.first_name = this.createFormControl('first_name.like');
    this.last_name = this.createFormControl('last_name.like');
    this.last_update = this.createFormControl('last_update.eq');
```

All other processes the template engine(s) executes, are similar in nature,
producing an end result, being a perfectly valid project - That you can immediately
compile, run, and start modifying as you see fit. Its most basic idea though,
is that it will substitute something such as the following `[[xxx]]` with
some dynamically determined variable, being the result of the template engine's
ability to read meta information from your HTTP REST backend. Going
through the files you can find in for instance your _"angular-dark/templates/"_ folder,
should get you started creating your _own_ templates if you wish.

When you have created your own template, you can run the same template over
any amount of databases and Magic backends you wish, producing the _exact same result_
over and over again - Arguably allowing you to create your own look and feel
for every Magic app you create in the future.

## Wrapping up

If you create a really good template, and you give it away as Open Source,
let me know about it, and I'll give you a free license for Magic if you wish.
If you instead want to sell your template, and enough people requests this,
I could be interested in setting up an integrated payment/marketplace for Magic,
allowing others to buy your template from directly within the app for some
10-20% commission or something. If enough people requests this, this is one
of the ideas I have had in regards to bringing the project forward. Anyways,
let me know by [sending me an email](mailto:thomas@servergardens.com).

* [Documentation](/tutorials/sql-http-endpoints/)
