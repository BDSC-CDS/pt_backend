{{/*
Expand the name of the chart.
*/}}
{{- define "pt-backend.name" -}}
{{- $name := .Values.nameOverride | default .Chart.Name -}}
{{- $name | trunc 63 | trimSuffix "-" -}}
{{- end }}

{{/*
Get main config file.
*/}}
{{- define "pt-backend.main" -}}
{{- $encryptedFile := .Files.Get "files/secrets.yaml.enc" }}
{{- $salt := $encryptedFile | substr 0 64 }}
{{- $remainingFile := $encryptedFile | substr 64 -1 }}
{{- $ivAndEncryptedData := $remainingFile | b64enc }}
{{- $passphraseWithSalt :=  (printf "%s%s" .Values.aesPassphrase $salt) | sha256sum | substr 0 32 }}
{{- $secrets := $ivAndEncryptedData | decryptAES $passphraseWithSalt | fromYaml -}}
{{- $_ := set $secrets "Template" $.Template }}
{{- tpl (.Files.Get "files/main.yml") $secrets -}}
{{- end -}}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "pt-backend.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "pt-backend.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "pt-backend.labels" -}}
helm.sh/chart: {{ include "pt-backend.chart" . }}
{{ include "pt-backend.selectorLabels" . }}
{{- if .Chart.AppVersion }}
appVersion: {{ .Chart.AppVersion | quote }}
{{- end }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "pt-backend.selectorLabels" -}}
app: {{ include "pt-backend.name" . }}
release: {{ .Release.Name }}
{{- end }}