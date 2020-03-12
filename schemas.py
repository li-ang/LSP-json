schemas = [
  {
    "name": ".angular-cli.json",
    "description": "Angular CLI configuration file",
    "fileMatch": [".angular-cli.json", "angular-cli.json"],
    "url": "https://raw.githubusercontent.com/angular/angular-cli/master/packages/angular/cli/lib/config/schema.json"
  },
  {
    "name": "Ansible",
    "description": "Ansible task files",
    "url": "http://json.schemastore.org/ansible-stable-2.9",
    "fileMatch": ["tasks/*.yml", "tasks/*.yaml"],
    "versions": {
      "2.0": "http://json.schemastore.org/ansible-stable-2.0",
      "2.1": "http://json.schemastore.org/ansible-stable-2.1",
      "2.2": "http://json.schemastore.org/ansible-stable-2.2",
      "2.3": "http://json.schemastore.org/ansible-stable-2.3",
      "2.4": "http://json.schemastore.org/ansible-stable-2.4",
      "2.5": "http://json.schemastore.org/ansible-stable-2.5",
      "2.6": "http://json.schemastore.org/ansible-stable-2.6",
      "2.7": "http://json.schemastore.org/ansible-stable-2.7",
      "2.9": "http://json.schemastore.org/ansible-stable-2.9"
    }
  },
  {
    "name": "apple-app-site-association",
    "description": "Apple Universal Link, App Site Association",
    "fileMatch": ["apple-app-site-association"],
    "url": "http://json.schemastore.org/apple-app-site-association"
  },
  {
    "name": "appsscript.json",
    "description": "Google Apps Script manifest file",
    "fileMatch": ["appsscript.json"],
    "url": "http://json.schemastore.org/appsscript"
  },
  {
    "name": "appsettings.json",
    "description": "ASP.NET Core's configuration file",
    "fileMatch": ["appsettings.json", "appsettings.*.json"],
    "url": "http://json.schemastore.org/appsettings"
  },
  {
    "name": "appveyor.yml",
    "description": "AppVeyor CI configuration file",
    "fileMatch": ["appveyor.yml"],
    "url": "http://json.schemastore.org/appveyor"
  },
  {
    "name": "arc.json",
    "description": "A JSON schema for OpenJS Architect",
    "fileMatch": ["arc.json", "arc.yml", "arc.yaml"],
    "url": "https://raw.githubusercontent.com/architect/parser/master/schema.json"
  },
  {
    "name": "Avro Avsc",
    "description": "Avro Schema Avsc file",
    "fileMatch": [".avsc"],
    "url": "http://json.schemastore.org/avro-avsc"
  },
  {
    "name": "Azure IoT Edge deployment",
    "description": "Azure IoT Edge deployment schema",
    "url": "http://json.schemastore.org/azure-iot-edge-deployment-2.0",
    "versions": {
      "1.0": "http://json.schemastore.org/azure-iot-edge-deployment-1.0",
      "1.1": "http://json.schemastore.org/azure-iot-edge-deployment-2.0"
    }
  },
  {
    "name": "Azure IoT Edge deployment template",
    "description": "Azure IoT Edge deployment template schema",
    "fileMatch": ["deployment.template.json", "deployment.*.template.json"],
    "url": "http://json.schemastore.org/azure-iot-edge-deployment-template-2.0",
    "versions": {
      "1.0": "http://json.schemastore.org/azure-iot-edge-deployment-template-1.0",
      "1.1": "http://json.schemastore.org/azure-iot-edge-deployment-template-2.0"
    }
  },
  {
    "name": "Foxx Manifest",
    "description": "ArangoDB Foxx service manifest file",
    "fileMatch": ["manifest.json"],
    "url": "http://json.schemastore.org/foxx-manifest"
  },
  {
    "name": ".asmdef",
    "description": "Unity 3D assembly definition file",
    "fileMatch": ["*.asmdef"],
    "url": "http://json.schemastore.org/asmdef"
  },
  {
    "name": "babelrc.json",
    "description": "Babel configuration file",
    "fileMatch": [".babelrc", "babel.config.json"],
    "url": "http://json.schemastore.org/babelrc"
  },
  {
    "name": ".backportrc.json",
    "description": "Backport configuration file",
    "fileMatch": [".backportrc.json"],
    "url": "http://json.schemastore.org/backportrc"
  },
  {
    "name": "batect.yml",
    "description": "batect configuration file",
    "fileMatch": ["batect.yml"],
    "url": "https://batect.dev/configSchema.json"
  },
  {
    "name": ".bootstraprc",
    "description": "Webpack bootstrap-loader configuration file",
    "fileMatch": [".bootstraprc"],
    "url": "http://json.schemastore.org/bootstraprc"
  },
  {
    "name": "bower.json",
    "description": "Bower package description file",
    "fileMatch": ["bower.json", ".bower.json"],
    "url": "http://json.schemastore.org/bower"
  },
  {
    "name": ".bowerrc",
    "description": "Bower configuration file",
    "fileMatch": [".bowerrc"],
    "url": "http://json.schemastore.org/bowerrc"
  },
  {
    "name": "behat.yml",
    "description": "Behat configuration file",
    "fileMatch": ["behat.yml", "*.behat.yml"],
    "url": "http://json.schemastore.org/behat"
  },
  {
    "name": "bozr.suite.json",
    "description": "Bozr test suite file",
    "fileMatch": [".suite.json", ".xsuite.json"],
    "url": "http://json.schemastore.org/bozr"
  },
  {
    "name": "bucklescript",
    "description": "BuckleScript configuration file",
    "fileMatch": ["bsconfig.json"],
    "url": "https://bucklescript.github.io/bucklescript/docson/build-schema.json"
  },
  {
    "name": "Bukkit plugin.yml",
    "description": "Schema for Minecraft Bukkit plugin description files",
    "fileMatch": ["plugin.yml"],
    "url": "http://json.schemastore.org/bukkit-plugin"
  },
  {
    "name": "Buildkite",
    "description": "Schema for Buildkite pipeline.yml files",
    "fileMatch": [
      "buildkite.yml",
      "buildkite.yaml",
      "buildkite.json",
      "buildkite.*.yml",
      "buildkite.*.yaml",
      "buildkite.*.json",
      ".buildkite/pipeline.yml",
      ".buildkite/pipeline.yaml",
      ".buildkite/pipeline.json",
      ".buildkite/pipeline.*.yml",
      ".buildkite/pipeline.*.yaml",
      ".buildkite/pipeline.*.json"
    ],
    "url": "https://raw.githubusercontent.com/buildkite/pipeline-schema/master/schema.json"
  },
  {
    "name": ".build.yml",
    "description": "Sourcehut Build Manifest",
    "fileMatch": [".build.yml"],
    "url": "http://json.schemastore.org/sourcehut-build"
  },
  {
    "name": "bundleconfig.json",
    "description": "Schema for bundleconfig.json files",
    "fileMatch": ["bundleconfig.json"],
    "url": "http://json.schemastore.org/bundleconfig"
  },
  {
    "name": "BungeeCord plugin.yml",
    "description": "Schema for BungeeCord plugin description files",
    "fileMatch": ["plugin.yml", "bungee.yml"],
    "url": "http://json.schemastore.org/bungee-plugin"
  },
  {
    "name": "Carafe",
    "description": "Schema for Carafe compatible JavaScript Bundles",
    "url": "https://carafe.fm/schema/draft-01/bundle.schema.json",
    "versions": {
      "draft-01": "https://carafe.fm/schema/draft-01/bundle.schema.json"
    }
  },
  {
    "name": "circleciconfig.json",
    "description": "Schema for CircleCI 2.0 config files",
    "fileMatch": [".circleci/config.yml"],
    "url": "http://json.schemastore.org/circleciconfig"
  },
  {
    "name": ".cirrus.yml",
    "description": "Cirrus CI configuration files",
    "fileMatch": [".cirrus.yml"],
    "url": "http://json.schemastore.org/cirrus"
  },
  {
    "name": ".clasp.json",
    "description": "Google Apps Script CLI project file",
    "fileMatch": [".clasp.json"],
    "url": "http://json.schemastore.org/clasp"
  },
  {
    "name": "JSON schema for Codecov configuration files",
    "description": "Schema for codecov.yml files.",
    "fileMatch": [".codecov.yml", "codecov.yml"],
    "url": "http://json.schemastore.org/codecov"
  },
  {
    "name": "compilerconfig.json",
    "description": "Schema for compilerconfig.json files",
    "fileMatch": ["compilerconfig.json"],
    "url": "http://json.schemastore.org/compilerconfig"
  },
  {
    "name": "compile_commands.json",
    "description": "LLVM compilation database",
    "fileMatch": ["compile_commands.json"],
    "url": "http://json.schemastore.org/compile-commands"
  },
  {
    "name": "commands.json",
    "description": "Config file for Command Task Runner",
    "fileMatch": ["commands.json"],
    "url": "http://json.schemastore.org/commands"
  },
  {
    "name": "cosmos.config.json",
    "description": "React Cosmos configuration file",
    "fileMatch": ["cosmos.config.json"],
    "url": "http://json.schemastore.org/cosmos-config"
  },
  {
    "name": "Chrome Extension",
    "description": "Google Chrome extension manifest file",
    "url": "http://json.schemastore.org/chrome-manifest"
  },
  {
    "name": "chutzpah.json",
    "description": "Chutzpah configuration file",
    "fileMatch": ["chutzpah.json"],
    "url": "http://json.schemastore.org/chutzpah"
  },
  {
    "name": "contentmanifest.json",
    "description": "Visual Studio manifest injection file",
    "fileMatch": ["contentmanifest.json"],
    "url": "http://json.schemastore.org/vsix-manifestinjection"
  },
  {
    "name": "cloud-sdk-pipeline-config-schema",
    "description": "SAP Cloud SDK Pipeline configuration",
    "fileMatch": ["pipeline_config.yml"],
    "url": "http://json.schemastore.org/cloud-sdk-pipeline-config-schema.json"
  },
  {
    "name": "cloudbuild.json",
    "description": "Google Cloud Build configuration file",
    "fileMatch": [
      "cloudbuild.json",
      "cloudbuild.yaml",
      "cloudbuild.yml",
      "*.cloudbuild.json",
      "*.cloudbuild.yaml",
      "*.cloudbuild.yml"
    ],
    "url": "http://json.schemastore.org/cloudbuild"
  },
  {
    "name": "AWS CloudFormation",
    "description": "AWS CloudFormation provides a common language for you to describe and provision all the infrastructure resources in your cloud environment.",
    "fileMatch": [
      "*.cf.json",
      "*.cf.yml",
      "*.cf.yaml",
      "cloudformation.json",
      "cloudformation.yml",
      "cloudformation.yaml"
    ],
    "url": "https://raw.githubusercontent.com/awslabs/goformation/master/schema/cloudformation.schema.json"
  },
  {
    "name": "AWS CloudFormation Serverless Application Model (SAM)",
    "description": "The AWS Serverless Application Model (AWS SAM, previously known as Project Flourish) extends AWS CloudFormation to provide a simplified way of defining the Amazon API Gateway APIs, AWS Lambda functions, and Amazon DynamoDB tables needed by your serverless application.",
    "fileMatch": [
      "*.sam.json",
      "*.sam.yml",
      "*.sam.yaml",
      "sam.json",
      "sam.yml",
      "sam.yaml"
    ],
    "url": "https://raw.githubusercontent.com/awslabs/goformation/master/schema/sam.schema.json"
  },
  {
    "name": "coffeelint.json",
    "description": "CoffeeLint configuration file",
    "fileMatch": ["coffeelint.json"],
    "url": "http://json.schemastore.org/coffeelint"
  },
  {
    "name": "composer.json",
    "description": "PHP Composer configuration file",
    "fileMatch": ["composer.json"],
    "url": "http://json.schemastore.org/composer"
  },
  {
    "name": "component.json",
    "description": "Web component file",
    "fileMatch": ["component.json"],
    "url": "http://json.schemastore.org/component"
  },
  {
    "name": "config.json",
    "description": "ASP.NET project config file",
    "fileMatch": ["config.json"],
    "url": "http://json.schemastore.org/config"
  },
  {
    "name": "contribute.json",
    "description": "A JSON schema for open-source project contribution data by Mozilla",
    "fileMatch": ["contribute.json"],
    "url": "http://json.schemastore.org/contribute"
  },
  {
    "name": "cypress.json",
    "description": "Cypress.io test runner configuration file",
    "fileMatch": ["cypress.json"],
    "url": "https://raw.githubusercontent.com/cypress-io/cypress/develop/cli/schema/cypress.schema.json"
  },
  {
    "name": ".creatomic",
    "description": "A config for Atomic Design 4 React generator",
    "fileMatch": [".creatomic"],
    "url": "http://json.schemastore.org/creatomic"
  },
  {
    "name": "cspell",
    "description": "JSON schema for cspell configuration file",
    "fileMatch": [".cspell.json", "cspell.json", "cSpell.json"],
    "url": "https://raw.githubusercontent.com/streetsidesoftware/cspell/master/cspell.schema.json"
  },
  {
    "name": ".csscomb.json",
    "description": "A JSON schema CSS Comb's configuration file",
    "fileMatch": [".csscomb.json"],
    "url": "http://json.schemastore.org/csscomb"
  },
  {
    "name": ".csslintrc",
    "description": "A JSON schema CSS Lint's configuration file",
    "fileMatch": [".csslintrc"],
    "url": "http://json.schemastore.org/csslintrc"
  },
  {
    "name": "datalogic-scan2deploy-android",
    "description": "Datalogic Scan2Deploy Android file",
    "fileMatch": [".dla.json"],
    "url": "http://json.schemastore.org/datalogic-scan2deploy-android"
  },
  {
    "name": "datalogic-scan2deploy-ce",
    "description": "Datalogic Scan2Deploy CE file",
    "fileMatch": [".dlc.json"],
    "url": "http://json.schemastore.org/datalogic-scan2deploy-ce"
  },
  {
    "name": "debugsettings.json",
    "description": "A JSON schema for the ASP.NET DebugSettings.json files",
    "fileMatch": ["debugsettings.json"],
    "url": "http://json.schemastore.org/debugsettings"
  },
  {
    "name": "dependabot.json",
    "description": "A JSON schema for the Dependabot config.yml files",
    "fileMatch": [".dependabot/config.yml"],
    "url": "http://json.schemastore.org/dependabot"
  },
  {
    "name": "docfx.json",
    "description": "A JSON schema for DocFx configuraton files",
    "fileMatch": ["docfx.json"],
    "url": "http://json.schemastore.org/docfx",
    "versions": {
      "2.8.0": "http://json.schemastore.org/docfx-2.8.0"
    }
  },
  {
    "name": "Dolittle Artifacts",
    "description": "A JSON schema for a Dolittle bounded context's artifacts",
    "fileMatch": [".dolittle/artifacts.json"],
    "url": "https://raw.githubusercontent.com/dolittle/DotNET.SDK/master/Schemas/Artifacts.Configuration/artifacts.json"
  },
  {
    "name": "Dolittle Bounded Context Configuration",
    "description": "A JSON schema for Dolittle application's bounded context configuration",
    "fileMatch": ["bounded-context.json"],
    "url": "https://raw.githubusercontent.com/dolittle/Runtime/master/Schemas/Applications.Configuration/bounded-context.json"
  },
  {
    "name": "Dolittle Event Horizons Configuration",
    "description": "A JSON schema for a Dolittle bounded context's event horizon configurations",
    "fileMatch": [".dolittle/event-horizons.json"],
    "url": "https://raw.githubusercontent.com/dolittle/Runtime/master/Schemas/Events/event-horizons.json"
  },
  {
    "name": "Dolittle Resources Configuration",
    "description": "A JSON schema for a Dolittle bounded context's resource configurations",
    "fileMatch": [".dolittle/resources.json"],
    "url": "https://raw.githubusercontent.com/dolittle/DotNET.Fundamentals/master/Schemas/ResourceTypes.Configuration/resources.json"
  },
  {
    "name": "Dolittle Server Configuration",
    "description": "A JSON schema for a Dolittle bounded context's event horizon's interaction server configuration",
    "fileMatch": [".dolittle/server.json"],
    "url": "https://raw.githubusercontent.com/dolittle/Runtime/master/Schemas/Server/server.json"
  },
  {
    "name": "Dolittle Tenants Configuration",
    "description": "A JSON schema for a Dolittle bounded context's tenant configuration",
    "fileMatch": [".dolittle/tenants.json"],
    "url": "https://raw.githubusercontent.com/dolittle/Runtime/master/Schemas/Tenancy/tenants.json"
  },
  {
    "name": "Dolittle Tenant Map Configuration",
    "description": "A JSON schema for a Dolittle bounded context's tenant mapping configurations",
    "fileMatch": [".dolittle/tenant-map.json"],
    "url": "https://raw.githubusercontent.com/dolittle/DotNET.Fundamentals/master/Schemas/Tenancy.Configuration/tenant-map.json"
  },
  {
    "name": "Dolittle Topology",
    "description": "A JSON schema for a Dolittle bounded context's topology",
    "fileMatch": [".dolittle/topology.json"],
    "url": "https://raw.githubusercontent.com/dolittle/DotNET.SDK/master/Schemas/Applications.Configuration/topology.json"
  },
  {
    "name": "dotnetcli.host.json",
    "description": "JSON schema for .NET CLI template host files",
    "fileMatch": ["dotnetcli.host.json"],
    "url": "http://json.schemastore.org/dotnetcli.host"
  },
  {
    "name": "drone.json",
    "description": "Drone CI configuration file",
    "fileMatch": [ ".drone.yml" ],
    "url": "http://json.schemastore.org/drone"
  },
  {
    "name": "Drush site aliases",
    "description": "JSON Schema for Drush 9 site aliases file",
    "fileMatch": ["sites/*.site.yml"],
    "url": "http://json.schemastore.org/drush.site.yml"
  },
  {
    "name": "dss-2.0.0.json",
    "description": "Digital Signature Service Core Protocols, Elements, and Bindings Version 2.0",
    "url": "http://json.schemastore.org/dss-2.0.0.json"
  },
  {
    "name": "Esquio",
    "description": "JSON schema for Esquio configuration files",
    "url": "http://json.schemastore.org/esquio"
  },
  {
    "name": "epr-manifest.json",
    "description": "Entry Point Regulation manifest file",
    "fileMatch": ["epr-manifest.json"],
    "url": "http://json.schemastore.org/epr-manifest"
  },
  {
    "name": "electron-builder configuration file.",
    "description": "JSON schema for electron-build configuration file.",
    "fileMatch": ["electron-builder.json"],
    "url": "http://json.schemastore.org/electron-builder"
  },
  {
    "name": ".eslintrc",
    "description": "JSON schema for ESLint configuration files",
    "fileMatch": [
      ".eslintrc",
      ".eslintrc.json",
      ".eslintrc.yml",
      ".eslintrc.yaml"
    ],
    "url": "http://json.schemastore.org/eslintrc"
  },
  {
    "name": "fabric.mod.json",
    "description": "Metadata file used by the Fabric mod loader",
    "fileMatch": ["fabric.mod.json"],
    "url": "http://json.schemastore.org/fabric-mod-json"
  },
  {
    "name": "Fantomas",
    "description": "Fantomas configuration file",
    "fileMatch": ["fantomas-config.json"],
    "url": "http://json.schemastore.org/fantomas"
  },
  {
    "name": "function.json",
    "description": "JSON schema for Azure Functions function.json files",
    "fileMatch": ["function.json"],
    "url": "http://json.schemastore.org/function"
  },
  {
    "name": "geojson.json",
    "description": "GeoJSON format for representing geographic data.",
    "url": "http://json.schemastore.org/geojson"
  },
  {
    "name": "GitHub Action",
    "description": "YAML schema for GitHub Actions",
    "fileMatch": ["action.yml"],
    "url": "http://json.schemastore.org/github-action"
  },
  {
    "name": "GitHub Workflow",
    "description": "YAML schema for GitHub Workflow",
    "fileMatch": [".github/workflows/**.yml", ".github/workflows/**.yaml"],
    "url": "http://json.schemastore.org/github-workflow"
  },
  {
    "name": "gitlab-ci",
    "description": "JSON schema for configuring Gitlab CI",
    "fileMatch": [".gitlab-ci.yml"],
    "url": "http://json.schemastore.org/gitlab-ci"
  },
  {
    "name": "Gitpod Configuration",
    "description": "JSON schema for configuring Gitpod.io",
    "fileMatch": [".gitpod.yml"],
    "url": "https://gitpod.io/schemas/gitpod-schema.json"
  },
  {
    "name": "global.json",
    "description": "ASP.NET global configuration file",
    "fileMatch": ["global.json"],
    "url": "http://json.schemastore.org/global"
  },
  {
    "name": "Grunt copy task",
    "description": "Grunt copy task configuration file",
    "fileMatch": ["copy.json"],
    "url": "http://json.schemastore.org/grunt-copy-task"
  },
  {
    "name": "Grunt clean task",
    "description": "Grunt clean task configuration file",
    "fileMatch": ["clean.json"],
    "url": "http://json.schemastore.org/grunt-clean-task"
  },
  {
    "name": "Grunt cssmin task",
    "description": "Grunt cssmin task configuration file",
    "fileMatch": ["cssmin.json"],
    "url": "http://json.schemastore.org/grunt-cssmin-task"
  },
  {
    "name": "Grunt JSHint task",
    "description": "Grunt JSHint task configuration file",
    "fileMatch": ["jshint.json"],
    "url": "http://json.schemastore.org/grunt-jshint-task"
  },
  {
    "name": "Grunt Watch task",
    "description": "Grunt Watch task configuration file",
    "fileMatch": ["watch.json"],
    "url": "http://json.schemastore.org/grunt-watch-task"
  },
  {
    "name": "Grunt base task",
    "description": "Schema for standard Grunt tasks",
    "fileMatch": ["grunt/*.json", "*-tasks.json"],
    "url": "http://json.schemastore.org/grunt-task"
  },
  {
    "name": "haxelib.json",
    "description": "Haxelib manifest",
    "fileMatch": ["haxelib.json"],
    "url": "http://json.schemastore.org/haxelib"
  },
  {
    "name": "host.json",
    "description": "JSON schema for Azure Functions host.json files",
    "fileMatch": ["host.json"],
    "url": "http://json.schemastore.org/host"
  },
  {
    "name": "host-meta.json",
    "description": "Schema for host-meta JDR files",
    "fileMatch": ["host-meta.json"],
    "url": "http://json.schemastore.org/host-meta"
  },
  {
    "name": ".htmlhintrc",
    "description": "HTML Hint configuration file",
    "fileMatch": [".htmlhintrc"],
    "url": "http://json.schemastore.org/htmlhint"
  },
  {
    "name": "imageoptimizer.json",
    "description": "Schema for imageoptimizer.json files",
    "fileMatch": ["imageoptimizer.json"],
    "url": "http://json.schemastore.org/imageoptimizer"
  },
  {
    "name": "Jekyll configuration",
    "description": "Schema for Jekyll _config.yml",
    "fileMatch": ["_config.yml"],
    "url": "http://json.schemastore.org/jekyll"
  },
  {
    "name": "Jenkins X Pipelines",
    "description": "Jenkins X Pipeline YAML configuration files",
    "fileMatch": ["jenkins-x*.yml"],
    "url": "https://jenkins-x.io/schemas/jx-schema.json"
  },
  {
    "name": "Jenkins X Requirements",
    "description": "Jenkins X Requirements YAML configuration file",
    "fileMatch": ["jx-requirements.yml"],
    "url": "https://jenkins-x.io/schemas/jx-requirements.json"
  },
  {
    "name": ".jsbeautifyrc",
    "description": "js-beautify configuration file",
    "fileMatch": [".jsbeautifyrc"],
    "url": "http://json.schemastore.org/jsbeautifyrc"
  },
  {
    "name": ".jsbeautifyrc-nested",
    "description": "js-beautify configuration file allowing nested `js`, `css`, and `html` attributes",
    "fileMatch": [".jsbeautifyrc"],
    "url": "http://json.schemastore.org/jsbeautifyrc-nested"
  },
  {
    "name": ".jscsrc",
    "description": "JSCS configuration file",
    "fileMatch": [".jscsrc", "jscsrc.json"],
    "url": "http://json.schemastore.org/jscsrc"
  },
  {
    "name": ".jshintrc",
    "description": "JSHint configuration file",
    "fileMatch": [".jshintrc"],
    "url": "http://json.schemastore.org/jshintrc"
  },
  {
    "name": ".jsinspectrc",
    "description": "JSInspect configuration file",
    "fileMatch": [".jsinspectrc"],
    "url": "http://json.schemastore.org/jsinspectrc"
  },
  {
    "name": "JSON-API",
    "description": "JSON API document",
    "fileMatch": ["*.schema.json"],
    "url": "http://jsonapi.org/schema"
  },
  {
    "name": "JSON Document Transform",
    "description": "JSON Document Transofrm",
    "url": "http://json.schemastore.org/jdt"
  },
  {
    "name": "JSON Feed",
    "description": "JSON schema for the JSON Feed format",
    "fileMatch": ["feed.json"],
    "url": "http://json.schemastore.org/feed"
  },
  {
    "name": "*.jsonld",
    "description": "JSON Linked Data files",
    "fileMatch": ["*.jsonld"],
    "url": "http://json.schemastore.org/jsonld"
  },
  {
    "name": "JSONPatch",
    "description": "JSONPatch files",
    "fileMatch": ["*.patch"],
    "url": "http://json.schemastore.org/json-patch"
  },
  {
    "name": "jsconfig.json",
    "description": "JavaScript project configuration file",
    "fileMatch": ["jsconfig.json"],
    "url": "http://json.schemastore.org/jsconfig"
  },
  {
    "name": "kustomization.yaml",
    "description": "Kubernetes native configuration management",
    "fileMatch": ["kustomization.yaml", "kustomization.yml"],
    "url": "http://json.schemastore.org/kustomization"
  },
  {
    "name": "launchsettings.json",
    "description": "A JSON schema for the ASP.NET LaunchSettings.json files",
    "fileMatch": ["launchsettings.json"],
    "url": "http://json.schemastore.org/launchsettings"
  },
  {
    "name": "lerna.json",
    "description": "A JSON schema for lerna.json files",
    "fileMatch": ["lerna.json"],
    "url": "http://json.schemastore.org/lerna"
  },
  {
    "name": "libman.json",
    "description": "JSON schema for client-side library config files",
    "fileMatch": ["libman.json"],
    "url": "http://json.schemastore.org/libman"
  },
  {
    "name": "lsdlschema.json",
    "description": "JSON schema for Linguistic Schema Definition Language files",
    "fileMatch": ["*.lsdl.yaml", "*.lsdl.json"],
    "url": "http://json.schemastore.org/lsdlschema"
  },
  {
    "name": "Microsoft Band Web Tile",
    "description": "Microsoft Band Web Tile manifest file",
    "url": "http://json.schemastore.org/band-manifest"
  },
  {
    "name": "mimetypes.json",
    "description": "JSON Schema for mime type collections",
    "fileMatch": ["mimetypes.json"],
    "url": "http://json.schemastore.org/mimetypes"
  },
  {
    "name": ".modernizrrc",
    "description": "Webpack modernizr-loader configuration file",
    "fileMatch": [".modernizrrc"],
    "url": "http://json.schemastore.org/modernizrrc"
  },
  {
    "name": "mycode.json",
    "description": "JSON schema for mycode.js files",
    "fileMatch": ["mycode.json"],
    "url": "http://json.schemastore.org/mycode"
  },
  {
    "name": "ninjs (News in JSON)",
    "description": "A JSON Schema for ninjs by the IPTC. News and publishing information. See https://iptc.org/standards/ninjs/",
    "url": "http://json.schemastore.org/ninjs-1.2.json",
    "versions": {
      "1.2": "http://json.schemastore.org/ninjs-1.2.json",
      "1.1": "http://json.schemastore.org/ninjs-1.1.json",
      "1.0": "http://json.schemastore.org/ninjs-1.0.json"
    }
  },
  {
    "name": ".nodehawkrc",
    "description": "JSON schema for .nodehawkrc configuration files.",
    "url": "http://json.schemastore.org/nodehawkrc",
    "fileMatch": [".nodehawkrc"]
  },
  {
    "name": "nodemon.json",
    "description": "JSON schema for nodemon.json configuration files.",
    "url": "http://json.schemastore.org/nodemon",
    "fileMatch": ["nodemon.json"]
  },
  {
    "name": ".npmpackagejsonlintrc",
    "description": "Configuration file for npm-package-json-lint",
    "fileMatch": [
      ".npmpackagejsonlintrc",
      "npmpackagejsonlintrc.json",
      ".npmpackagejsonlintrc.json"
    ],
    "url": "http://json.schemastore.org/npmpackagejsonlintrc"
  },
  {
    "name": "nuget-project.json",
    "description": "JSON schema for NuGet project.json files.",
    "url": "http://json.schemastore.org/nuget-project",
    "versions": {
      "3.3.0": "http://json.schemastore.org/nuget-project-3.3.0"
    }
  },
  {
    "name": "nswag.json",
    "description": "JSON schema for nswag configuration",
    "url": "http://json.schemastore.org/nswag",
    "fileMatch": ["nswag.json"]
  },
  {
    "name": "ocelot.json",
    "description": "JSON schema for the Ocelot Api Gateway.",
    "fileMatch": ["ocelot.json"],
    "url": "http://json.schemastore.org/ocelot"
  },
  {
    "name": "omnisharp.json",
    "description": "Omnisharp Configuration file",
    "fileMatch": ["omnisharp.json"],
    "url": "http://json.schemastore.org/omnisharp"
  },
  {
    "name": "openapi.json",
    "description": "A JSON schema for Open API documentation files",
    "fileMatch": ["openapi.json", "openapi.yml", "openapi.yaml"],
    "url": "https://raw.githubusercontent.com/OAI/OpenAPI-Specification/master/schemas/v3.0/schema.json"
  },
  {
    "name": "openfin.json",
    "description": "OpenFin application configuration file",
    "url": "http://json.schemastore.org/openfin"
  },
  {
    "name": "package.json",
    "description": "NPM configuration file",
    "fileMatch": ["package.json"],
    "url": "http://json.schemastore.org/package"
  },
  {
    "name": "package.manifest",
    "description": "Umbraco package configuration file",
    "fileMatch": ["package.manifest"],
    "url": "http://json.schemastore.org/package.manifest",
    "versions": {
      "8.0.0": "http://json.schemastore.org/package.manifest-8.0.0",
      "7.0.0": "http://json.schemastore.org/package.manifest-7.0.0"
    }
  },
  {
    "name": "pattern.json",
    "description": "Patternplate pattern manifest file",
    "fileMatch": ["pattern.json"],
    "url": "http://json.schemastore.org/pattern"
  },
  {
    "name": "PocketMine plugin.yml",
    "description": "PocketMine plugin manifest file",
    "fileMatch": ["plugin.yml"],
    "url": "http://json.schemastore.org/pocketmine-plugin"
  },
  {
    "name": ".phraseapp.yml",
    "description": "PhraseApp configuration file",
    "fileMatch": [".phraseapp.yml"],
    "url": "http://json.schemastore.org/phraseapp"
  },
  {
    "name": "prettierrc.json",
    "description": ".prettierrc configuration file",
    "fileMatch": [".prettierrc", ".prettierrc.json"],
    "url": "http://json.schemastore.org/prettierrc",
    "versions": {
      "1.8.2": "http://json.schemastore.org/prettierrc-1.8.2"
    }
  },
  {
    "name": "prisma.yml",
    "description": "prisma.yml service definition file",
    "fileMatch": ["prisma.yml"],
    "url": "http://json.schemastore.org/prisma"
  },
  {
    "name": "project.json",
    "description": "ASP.NET vNext project configuration file",
    "fileMatch": ["project.json"],
    "url": "http://json.schemastore.org/project",
    "versions": {
      "1.0.0-beta3": "http://json.schemastore.org/project-1.0.0-beta3",
      "1.0.0-beta4": "http://json.schemastore.org/project-1.0.0-beta4",
      "1.0.0-beta5": "http://json.schemastore.org/project-1.0.0-beta5",
      "1.0.0-beta6": "http://json.schemastore.org/project-1.0.0-beta6",
      "1.0.0-beta8": "http://json.schemastore.org/project-1.0.0-beta8",
      "1.0.0-rc1": "http://json.schemastore.org/project-1.0.0-rc1",
      "1.0.0-rc1-update1": "http://json.schemastore.org/project-1.0.0-rc1",
      "1.0.0-rc2": "http://json.schemastore.org/project-1.0.0-rc2"
    }
  },
  {
    "name": "project-1.0.0-beta3.json",
    "description": "ASP.NET vNext project configuration file",
    "url": "http://json.schemastore.org/project-1.0.0-beta3"
  },
  {
    "name": "project-1.0.0-beta4.json",
    "description": "ASP.NET vNext project configuration file",
    "url": "http://json.schemastore.org/project-1.0.0-beta4"
  },
  {
    "name": "project-1.0.0-beta5.json",
    "description": "ASP.NET vNext project configuration file",
    "url": "http://json.schemastore.org/project-1.0.0-beta5"
  },
  {
    "name": "project-1.0.0-beta6.json",
    "description": "ASP.NET vNext project configuration file",
    "url": "http://json.schemastore.org/project-1.0.0-beta6"
  },
  {
    "name": "project-1.0.0-beta8.json",
    "description": "ASP.NET vNext project configuration file",
    "url": "http://json.schemastore.org/project-1.0.0-beta8"
  },
  {
    "name": "project-1.0.0-rc1.json",
    "description": "ASP.NET vNext project configuration file",
    "url": "http://json.schemastore.org/project-1.0.0-rc1"
  },
  {
    "name": "project-1.0.0-rc2.json",
    "description": ".NET Core project configuration file",
    "url": "http://json.schemastore.org/project-1.0.0-rc2"
  },
  {
    "name": "prometheus.json",
    "description": "Prometheus configuration file",
    "fileMatch": ["prometheus.yml"],
    "url": "http://json.schemastore.org/prometheus"
  },
  {
    "name": "prometheus.rules.json",
    "description": "Prometheus rules file",
    "fileMatch": ["*.rules"],
    "url": "http://json.schemastore.org/prometheus.rules"
  },
  {
    "name": "proxies.json",
    "description": "JSON schema for Azure Function Proxies proxies.json files",
    "fileMatch": ["proxies.json"],
    "url": "http://json.schemastore.org/proxies"
  },
  {
    "name": "pubspec.yaml",
    "description": "Schema for pubspecs, the format used by Dart's dependency manager",
    "fileMatch": ["pubspec.yaml"],
    "url": "http://json.schemastore.org/pubspec"
  },
  {
    "name": "pyrseas-0.8.json",
    "description": "Pyrseas database schema versioning for Postgres databases, v0.8",
    "fileMatch": ["pyrseas-0.8.json"],
    "url": "http://json.schemastore.org/pyrseas-0.8"
  },
  {
    "name": "*.resjson",
    "description": "Windows App localization file",
    "fileMatch": ["*.resjson"],
    "url": "http://json.schemastore.org/resjson"
  },
  {
    "name": "JSON Resume",
    "description": "A JSON format to describe resumes",
    "fileMatch": ["resume.json"],
    "url": "http://json.schemastore.org/resume"
  },
  {
    "name": "Renovate",
    "description": "Renovate config file (https://github.com/renovatebot/renovate)",
    "fileMatch": [
      "renovate.json",
      "renovate.json5",
      ".github/renovate.json",
      ".github/renovate.json5",
      ".renovaterc",
      ".renovaterc.json"
    ],
    "url": "https://docs.renovatebot.com/renovate-schema.json"
  },
  {
    "name": "sarif-1.0.0.json",
    "description": "Static Analysis Results Interchange Format (SARIF) version 1",
    "url": "http://json.schemastore.org/sarif-1.0.0.json"
  },
  {
    "name": "sarif-2.0.0.json",
    "description": "Static Analysis Results Interchange Format (SARIF) version 2",
    "url": "http://json.schemastore.org/sarif-2.0.0.json"
  },
  {
    "name": "2.0.0-csd.2.beta.2018-10-10",
    "description": "Static Analysis Results Format (SARIF) Version 2.0.0-csd.2.beta-2018-10-10",
    "url": "http://json.schemastore.org/2.0.0-csd.2.beta.2018-10-10.json"
  },
  {
    "name": "sarif-2.1.0-rtm.2",
    "description": "Static Analysis Results Format (SARIF), Version 2.1.0-rtm.2",
    "url": "http://json.schemastore.org/sarif-2.1.0-rtm.2.json"
  },
  {
    "name": "sarif-external-property-file-2.1.0-rtm.2",
    "description": "Static Analysis Results Format (SARIF) External Property File Format, Version 2.1.0-rtm.2",
    "url": "http://json.schemastore.org/sarif-external-property-file-2.1.0-rtm.2.json"
  },
  {
    "name": "sarif-2.1.0-rtm.3",
    "description": "Static Analysis Results Format (SARIF), Version 2.1.0-rtm.3",
    "url": "http://json.schemastore.org/sarif-2.1.0-rtm.3.json"
  },
  {
    "name": "sarif-external-property-file-2.1.0-rtm.3",
    "description": "Static Analysis Results Format (SARIF) External Property File Format, Version 2.1.0-rtm.3",
    "url": "http://json.schemastore.org/sarif-external-property-file-2.1.0-rtm.3.json"
  },
  {
    "name": "sarif-2.1.0-rtm.4",
    "description": "Static Analysis Results Format (SARIF), Version 2.1.0-rtm.4",
    "url": "http://json.schemastore.org/sarif-2.1.0-rtm.4.json"
  },
  {
    "name": "sarif-external-property-file-2.1.0-rtm.4",
    "description": "Static Analysis Results Format (SARIF) External Property File Format, Version 2.1.0-rtm.4",
    "url": "http://json.schemastore.org/sarif-external-property-file-2.1.0-rtm.4.json"
  },
  {
    "name": "sarif-2.1.0-rtm.5",
    "description": "Static Analysis Results Format (SARIF), Version 2.1.0-rtm.5",
    "url": "http://json.schemastore.org/sarif-2.1.0-rtm.5.json"
  },
  {
    "name": "sarif-external-property-file-2.1.0-rtm.5",
    "description": "Static Analysis Results Format (SARIF) External Property File Format, Version 2.1.0-rtm.5",
    "url": "http://json.schemastore.org/sarif-external-property-file-2.1.0-rtm.5.json"
  },
  {
    "name": "Schema Catalog",
    "description": "JSON Schema catalog files compatible with SchemaStore.org",
    "url": "http://json.schemastore.org/schema-catalog"
  },
  {
    "name": "schema.org - Action",
    "description": "JSON Schema for Action as defined by schema.org",
    "url": "http://json.schemastore.org/schema-org-action"
  },
  {
    "name": "schema.org - ContactPoint",
    "description": "JSON Schema for ContactPoint as defined by schema.org",
    "url": "http://json.schemastore.org/schema-org-contact-point"
  },
  {
    "name": "schema.org - Place",
    "description": "JSON Schema for Place as defined by schema.org",
    "url": "http://json.schemastore.org/schema-org-place"
  },
  {
    "name": "schema.org - Thing",
    "description": "JSON Schema for Thing as defined by schema.org",
    "url": "http://json.schemastore.org/schema-org-thing"
  },
  {
    "name": "settings.job",
    "description": "Azure Webjob settings file",
    "fileMatch": ["settings.job"],
    "url": "http://json.schemastore.org/settings.job"
  },
  {
    "name": "skyuxconfig.json",
    "description": "SKY UX CLI configuration file",
    "fileMatch": ["skyuxconfig.json", "skyuxconfig.*.json"],
    "url": "https://raw.githubusercontent.com/blackbaud/skyux-builder/master/skyuxconfig-schema.json"
  },
  {
    "name": "snapcraft",
    "description": "snapcraft project  (https://snapcraft.io)",
    "fileMatch": [".snapcraft.yaml", "snapcraft.yaml"],
    "url": "https://raw.githubusercontent.com/snapcore/snapcraft/master/schema/snapcraft.json"
  },
  {
    "name": "Solidarity",
    "description": "CLI config for enforcing environment settings",
    "fileMatch": [".solidarity", ".solidarity.json"],
    "url": "http://json.schemastore.org/solidaritySchema"
  },
  {
    "name": "Source Maps v3",
    "description": "Source Map files version 3",
    "fileMatch": ["*.map"],
    "url": "http://json.schemastore.org/sourcemap-v3"
  },
  {
    "name": ".sprite files",
    "description": "Schema for image sprite generation files",
    "fileMatch": ["*.sprite"],
    "url": "http://json.schemastore.org/sprite"
  },
  {
    "name": "Stryker Mutator",
    "description": "Configuration file for Stryker Mutator, the mutation testing framework for JavaScript and friends. See https://stryker-mutator.io.",
    "fileMatch": ["stryker.conf.json", "stryker-*.conf.json"],
    "url": "https://raw.githubusercontent.com/stryker-mutator/stryker/master/packages/api/schema/stryker-core.json"
  },
  {
    "name": "StyleCop Analyzers Configuration",
    "description": "Configuration file for StyleCop Analyzers",
    "fileMatch": ["stylecop.json"],
    "url": "https://raw.githubusercontent.com/DotNetAnalyzers/StyleCopAnalyzers/master/StyleCop.Analyzers/StyleCop.Analyzers/Settings/stylecop.schema.json"
  },
  {
    "name": ".stylelintrc",
    "description": "Configuration file for stylelint",
    "fileMatch": [".stylelintrc", "stylelintrc.json", ".stylelintrc.json"],
    "url": "http://json.schemastore.org/stylelintrc"
  },
  {
    "name": "Swagger API 2.0",
    "description": "Swagger API 2.0 schema",
    "fileMatch": ["swagger.json"],
    "url": "http://json.schemastore.org/swagger-2.0"
  },
  {
    "name": "template.json",
    "description": "JSON schema .NET template files",
    "fileMatch": [".template.config/template.json"],
    "url": "http://json.schemastore.org/template"
  },
  {
    "name": "templatsources.json",
    "description": "SideWaffle template source schema",
    "fileMatch": ["templatesources.json"],
    "url": "http://json.schemastore.org/templatesources"
  },
  {
    "name": "tmLanguage",
    "description": "Language grammar description files in Textmate and compatible editors",
    "fileMatch": ["*.tmLanguage.json"],
    "url": "https://raw.githubusercontent.com/Septh/tmlanguage/master/tmLanguage.schema.json"
  },
  {
    "name": ".travis.yml",
    "description": "Travis CI configuration file",
    "fileMatch": [".travis.yml"],
    "url": "http://json.schemastore.org/travis"
  },
  {
    "name": "tsconfig.json",
    "description": "TypeScript compiler configuration file",
    "fileMatch": ["tsconfig.json"],
    "url": "http://json.schemastore.org/tsconfig"
  },
  {
    "name": "tsd.json",
    "description": "JSON schema for DefinatelyTyped description manager (TSD)",
    "fileMatch": ["tsd.json"],
    "url": "http://json.schemastore.org/tsd"
  },
  {
    "name": "tsdrc.json",
    "description": "TypeScript Definition manager (tsd) global settings file",
    "fileMatch": [".tsdrc"],
    "url": "http://json.schemastore.org/tsdrc"
  },
  {
    "name": "ts-force-config.json",
    "description": "Generated Typescript classes for Salesforce",
    "fileMatch": ["ts-force-config.json"],
    "url": "http://json.schemastore.org/ts-force-config"
  },
  {
    "name": "tslint.json",
    "description": "TypeScript Lint configuration file",
    "fileMatch": ["tslint.json", "tslint.yaml", "tslint.yml"],
    "url": "http://json.schemastore.org/tslint"
  },
  {
    "name": "typewiz.json",
    "description": "Typewiz configuration file",
    "fileMatch": ["typewiz.json"],
    "url": "http://json.schemastore.org/typewiz"
  },
  {
    "name": "typings.json",
    "description": "Typings TypeScript definitions manager definition file",
    "fileMatch": ["typings.json"],
    "url": "http://json.schemastore.org/typings"
  },
  {
    "name": "typingsrc.json",
    "description": "Typings TypeScript definitions manager configuration file",
    "fileMatch": [".typingsrc"],
    "url": "http://json.schemastore.org/typingsrc"
  },
  {
    "name": "up.json",
    "description": "Up configuration file",
    "fileMatch": ["up.json"],
    "url": "http://json.schemastore.org/up.json"
  },
  {
    "name": "ui5-manifest",
    "description": "UI5/OPENUI5 descriptor file",
    "fileMatch": [".manifest"],
    "url": "http://json.schemastore.org/ui5-manifest"
  },
  {
    "name": "vega.json",
    "description": "Vega visualization specification file",
    "fileMatch": ["*.vg", "*.vg.json"],
    "url": "http://json.schemastore.org/vega"
  },
  {
    "name": "vega-lite.json",
    "description": "Vega-Lite visualization specification file",
    "fileMatch": ["*.vl", "*.vl.json"],
    "url": "http://json.schemastore.org/vega-lite"
  },
  {
    "name": "version.json",
    "description": "A project version descriptor file used by Nerdbank.GitVersioning",
    "fileMatch": ["version.json"],
    "url": "https://raw.githubusercontent.com/AArnott/Nerdbank.GitVersioning/master/src/NerdBank.GitVersioning/version.schema.json"
  },
  {
    "name": "vsls.json",
    "description": "Visual Studio Live Share configuration file",
    "fileMatch": [".vsls.json"],
    "url": "http://json.schemastore.org/vsls"
  },
  {
    "name": "vs-2017.3.host.json",
    "description": "JSON schema for Visual Studio template host file",
    "fileMatch": ["vs-2017.3.host.json"],
    "url": "http://json.schemastore.org/vs-2017.3.host"
  },
  {
    "name": "vs-nesting.json",
    "description": "JSON schema for Visual Studio's file nesting feature",
    "fileMatch": ["*.filenesting.json", ".filenesting.json"],
    "url": "http://json.schemastore.org/vs-nesting"
  },
  {
    "name": ".vsconfig",
    "description": "JSON schema for Visual Studio component configuration files",
    "fileMatch": ["*.vsconfig"],
    "url": "http://json.schemastore.org/vsconfig"
  },
  {
    "name": ".vsext",
    "description": "JSON schema for Visual Studio extension pack manifests",
    "fileMatch": ["*.vsext"],
    "url": "http://json.schemastore.org/vsext"
  },
  {
    "name": "VSIX CLI publishing",
    "description": "JSON schema for Visual Studio extension publishing",
    "fileMatch": ["vs-publish.json"],
    "url": "http://json.schemastore.org/vsix-publish"
  },
  {
    "name": "vss-extension.json",
    "description": "JSON Schema for Azure DevOps Extensions",
    "fileMatch": ["vss-extension.json"],
    "url": "http://json.schemastore.org/vss-extension"
  },
  {
    "name": "WebExtensions",
    "description": "JSON schema for WebExtension manifest files",
    "fileMatch": ["manifest.json"],
    "url": "http://json.schemastore.org/webextension"
  },
  {
    "name": "Web Manifest",
    "description": "Web Application manifest file",
    "fileMatch": ["manifest.json", "*.webmanifest"],
    "url": "http://json.schemastore.org/web-manifest"
  },
  {
    "name": "webjobs-list.json",
    "description": "Azure Webjob list file",
    "fileMatch": ["webjobs-list.json"],
    "url": "http://json.schemastore.org/webjobs-list"
  },
  {
    "name": "webjobpublishsettings.json",
    "description": "Azure Webjobs publish settings file",
    "fileMatch": ["webjobpublishsettings.json"],
    "url": "http://json.schemastore.org/webjob-publish-settings"
  },
  {
    "name": "Web types",
    "description": "JSON standard for web component libraries metadata",
    "fileMatch": ["web-types.json", "*.web-types.json"],
    "url": "http://json.schemastore.org/web-types"
  },
  {
    "name": "JSON-stat 2.0",
    "description": "JSON-stat 2.0 Schema",
    "url": "https://json-stat.org/format/schema/2.0/"
  },
  {
    "name": "KSP-CKAN 1.26.4",
    "description": "Metadata spec v1.26.4 for KSP-CKAN",
    "fileMatch": ["*.ckan"],
    "url": "http://json.schemastore.org/ksp-ckan"
  },
  {
    "name": "JSON Schema Draft 4",
    "description": "Meta-validation schema for JSON Schema Draft 4",
    "url": "http://json-schema.org/draft-04/schema"
  },
  {
    "name": "xunit.runner.json",
    "description": "xUnit.net runner configuration file",
    "fileMatch": ["xunit.runner.json"],
    "url": "http://json.schemastore.org/xunit.runner.schema"
  },
  {
    "name": ".cryproj engine-5.2",
    "description": "A JSON schema for CRYENGINE projects (.cryproj files)",
    "fileMatch": ["*.cryproj"],
    "url": "http://json.schemastore.org/cryproj.52.schema"
  },
  {
    "name": ".cryproj engine-5.3",
    "description": "A JSON schema for CRYENGINE projects (.cryproj files)",
    "fileMatch": ["*.cryproj"],
    "url": "http://json.schemastore.org/cryproj.53.schema"
  },
  {
    "name": ".cryproj engine-5.4",
    "description": "A JSON schema for CRYENGINE projects (.cryproj files)",
    "fileMatch": ["*.cryproj"],
    "url": "http://json.schemastore.org/cryproj.54.schema"
  },
  {
    "name": ".cryproj engine-5.5",
    "description": "A JSON schema for CRYENGINE projects (.cryproj files)",
    "fileMatch": ["*.cryproj"],
    "url": "http://json.schemastore.org/cryproj.55.schema"
  },
  {
    "name": ".cryproj engine-dev",
    "description": "A JSON schema for CRYENGINE projects (.cryproj files)",
    "fileMatch": ["*.cryproj"],
    "url": "http://json.schemastore.org/cryproj.dev.schema"
  },
  {
    "name": ".cryproj (generic)",
    "description": "A JSON schema for CRYENGINE projects (.cryproj files)",
    "fileMatch": ["*.cryproj"],
    "url": "http://json.schemastore.org/cryproj"
  },
  {
    "name": "typedoc.json",
    "description": "A JSON schema for the Typedoc configuration file",
    "fileMatch": ["typedoc.json"],
    "url": "http://json.schemastore.org/typedoc"
  },
  {
    "name": "huskyrc",
    "description": "Husky can prevent bad `git commit`, `git push` and more 🐶 woof!",
    "fileMatch": [".huskyrc", ".huskyrc.json"],
    "url": "http://json.schemastore.org/huskyrc"
  },
  {
    "name": ".lintstagedrc",
    "description": "JSON schema for lint-staged config",
    "fileMatch": [".lintstagedrc", ".lintstagedrc.json"],
    "url": "http://json.schemastore.org/lintstagedrc.schema"
  },
  {
    "name": "mta.yaml",
    "description": "A JSON schema for MTA projects v3.3",
    "fileMatch": [ "mta.yaml", "mta.yml" ],
    "url": "http://json.schemastore.org/mta"
  },
  {
    "name": "mtad.yaml",
    "description": "A JSON schema for MTA deployment descriptors v3.3",
    "fileMatch": ["mtad.yaml", "mtad.yml"],
    "url": "http://json.schemastore.org/mtad"
  },
  {
    "name": ".mtaext",
    "description": "A JSON schema for MTA extension descriptors v3.3",
    "fileMatch": ["*.mtaext"],
    "url": "http://json.schemastore.org/mtaext"
  },
  {
    "name": "Opctl",
    "description": "Opctl schema for describing an op",
    "url": "http://json.schemastore.org/opspec-io-0.1.7",
    "fileMatch": [".opspec/*/*.yml", ".opspec/*/*.yaml"]
  },
  {
    "name": "HEMTT",
    "description": "HEMTT Project File",
    "url": "http://json.schemastore.org/hemtt-0.6.2",
    "fileMatch": ["hemtt.json", "hemtt.toml"],
    "versions": {
      "0.6.2": "http://json.schemastore.org/hemtt-0.6.2"
    }
  },
  {
    "name": "now",
    "description": "ZEIT Now project configuration file",
    "fileMatch": ["now.json"],
    "url": "http://json.schemastore.org/now"
  },
  {
    "name": "taskcat",
    "description": "taskcat",
    "fileMatch": [".taskcat.yml"],
    "url": "https://raw.githubusercontent.com/aws-quickstart/taskcat/master/taskcat/cfg/config_schema.json"
  },
  {
    "name": "BizTalkServerApplicationSchema",
    "description": "BizTalk server application inventory json file.",
    "fileMatch": ["BizTalkServerInventory.json"],
    "url": "http://json.schemastore.org/BizTalkServerApplicationSchema"
  },
  {
    "name": "httpmockrc",
    "description": "Http-mocker is a tool for mock local requests or proxy remote requests.",
    "fileMatch": [".httpmockrc", ".httpmock.json"],
    "url": "http://json.schemastore.org/httpmockrc"
  },
  {
    "name": "neoload",
    "description": "Neotys as-code load test specification, more at: https://github.com/Neotys-Labs/neoload-cli",
    "fileMatch": [".nl.yaml", ".nl.yml", ".nl.json", ".neoload.yaml", ".neoload.yml", ".neoload.json"],
    "url": "https://raw.githubusercontent.com/Neotys-Labs/neoload-cli/master/resources/as-code.latest.schema.json"
  },
  {
    "name": "release drafter",
    "description": "Release Drafter configuration file",
    "fileMatch": ["release-drafter.yml"],
    "url": "https://raw.githubusercontent.com/release-drafter/release-drafter/master/schema.json"
  },
  {
    "name": "zuul",
    "description": "Zuul CI configuration file",
    "fileMatch": ["*zuul.d/*.yaml", "*/.zuul.yaml"],
    "url": "https://raw.githubusercontent.com/pycontribs/zuul-lint/master/zuul_lint/zuul-schema.json"
  },
  {
    "name": "Briefcase",
    "description": "Microsoft Briefcase configuration file",
    "fileMatch": ["briefcase.yaml"],
    "url": "https://raw.githubusercontent.com/microsoft/Briefcase/master/mlbriefcase/briefcase-schema.json"
  },
  {
    "name": "httparchive",
    "description": "HTTP Archive",
    "fileMatch": ["*.har"],
    "url": "https://raw.githubusercontent.com/ahmadnassri/har-schema/master/lib/har.json"
  }
]
