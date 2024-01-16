# Hasura Data Connectors Developer's Guide

# Schema

The schema endpoint defines any types used by the data connector, and describes the collections and their columns, functions, and any procedures.

The schema endpoint is used to specify the behavior of a data connector, so that it can be tested, verified, and used by tools such as code generators. It is primarily provided by data connector implementors as a development and specification tool, and it is not expected to be used at "runtime", in the same sense that the `/query` and `/mutation` endpoints would be.

## Request

`GET /schema`

## Response

See[ SchemaResponse ](../../reference/types.html#schemaresponse)

### Example

```
{
"scalar_types"
: {
"Int"
: {
"aggregate_functions"
: {
"max"
: {
"result_type"
: {
"type"
:
"nullable"
,
"underlying_type"
: {
"type"
:
"named"
,
"name"
:
"Int"
}
          }
        },
"min"
: {
"result_type"
: {
"type"
:
"nullable"
,
"underlying_type"
: {
"type"
:
"named"
,
"name"
:
"Int"
}
          }
        }
      },
"comparison_operators"
: {}
    },
"String"
: {
"aggregate_functions"
: {},
"comparison_operators"
: {
"like"
: {
"argument_type"
: {
"type"
:
"named"
,
"name"
:
"String"
}
        }
      }
    }
  },
"object_types"
: {
"article"
: {
"description"
:
"An article"
,
"fields"
: {
"author_id"
: {
"description"
:
"The article's author ID"
,
"type"
: {
"type"
:
"named"
,
"name"
:
"Int"
}
        },
"id"
: {
"description"
:
"The article's primary key"
,
"type"
: {
"type"
:
"named"
,
"name"
:
"Int"
}
        },
"title"
: {
"description"
:
"The article's title"
,
"type"
: {
"type"
:
"named"
,
"name"
:
"String"
}
        }
      }
    },
"author"
: {
"description"
:
"An author"
,
"fields"
: {
"first_name"
: {
"description"
:
"The author's first name"
,
"type"
: {
"type"
:
"named"
,
"name"
:
"String"
}
        },
"id"
: {
"description"
:
"The author's primary key"
,
"type"
: {
"type"
:
"named"
,
"name"
:
"Int"
}
        },
"last_name"
: {
"description"
:
"The author's last name"
,
"type"
: {
"type"
:
"named"
,
"name"
:
"String"
}
        }
      }
    }
  },
"collections"
: [
    {
"name"
:
"articles"
,
"description"
:
"A collection of articles"
,
"arguments"
: {},
"type"
:
"article"
,
"uniqueness_constraints"
: {
"ArticleByID"
: {
"unique_columns"
: [
"id"
]
        }
      },
"foreign_keys"
: {
"Article_AuthorID"
: {
"column_mapping"
: {
"author_id"
:
"id"
},
"foreign_collection"
:
"authors"
}
      }
    },
    {
"name"
:
"authors"
,
"description"
:
"A collection of authors"
,
"arguments"
: {},
"type"
:
"author"
,
"uniqueness_constraints"
: {
"AuthorByID"
: {
"unique_columns"
: [
"id"
]
        }
      },
"foreign_keys"
: {}
    },
    {
"name"
:
"articles_by_author"
,
"description"
:
"Articles parameterized by author"
,
"arguments"
: {
"author_id"
: {
"type"
: {
"type"
:
"named"
,
"name"
:
"Int"
}
        }
      },
"type"
:
"article"
,
"uniqueness_constraints"
: {},
"foreign_keys"
: {}
    }
  ],
"functions"
: [
    {
"name"
:
"latest_article_id"
,
"description"
:
"Get the ID of the most recent article"
,
"arguments"
: {},
"result_type"
: {
"type"
:
"nullable"
,
"underlying_type"
: {
"type"
:
"named"
,
"name"
:
"Int"
}
      }
    }
  ],
"procedures"
: [
    {
"name"
:
"upsert_article"
,
"description"
:
"Insert or update an article"
,
"arguments"
: {
"article"
: {
"description"
:
"The article to insert or update"
,
"type"
: {
"type"
:
"named"
,
"name"
:
"article"
}
        }
      },
"result_type"
: {
"type"
:
"nullable"
,
"underlying_type"
: {
"type"
:
"named"
,
"name"
:
"article"
}
      }
    }
  ]
}
```

## Response Fields

| Name | Description |
|---|---|
|  `scalar_types`  | [ Scalar Types ](scalar-types.html) |
|  `object_types`  | [ Object Types ](object-types.html) |
|  `collections`  | [ Collection ](collections.html) |
|  `functions`  | [ Functions ](functions.html) |
|  `procedures`  | [ Procedures ](procedures.html) |
