// Code generated by go-swagger; DO NOT EDIT.

package pipeline_service

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"context"
	"net/http"
	"time"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/runtime"
	cr "github.com/go-openapi/runtime/client"

	strfmt "github.com/go-openapi/strfmt"
)

// NewCreatePipelineVersionParams creates a new CreatePipelineVersionParams object
// with the default values initialized.
func NewCreatePipelineVersionParams() *CreatePipelineVersionParams {
	var ()
	return &CreatePipelineVersionParams{

		timeout: cr.DefaultTimeout,
	}
}

// NewCreatePipelineVersionParamsWithTimeout creates a new CreatePipelineVersionParams object
// with the default values initialized, and the ability to set a timeout on a request
func NewCreatePipelineVersionParamsWithTimeout(timeout time.Duration) *CreatePipelineVersionParams {
	var ()
	return &CreatePipelineVersionParams{

		timeout: timeout,
	}
}

// NewCreatePipelineVersionParamsWithContext creates a new CreatePipelineVersionParams object
// with the default values initialized, and the ability to set a context for a request
func NewCreatePipelineVersionParamsWithContext(ctx context.Context) *CreatePipelineVersionParams {
	var ()
	return &CreatePipelineVersionParams{

		Context: ctx,
	}
}

// NewCreatePipelineVersionParamsWithHTTPClient creates a new CreatePipelineVersionParams object
// with the default values initialized, and the ability to set a custom HTTPClient for a request
func NewCreatePipelineVersionParamsWithHTTPClient(client *http.Client) *CreatePipelineVersionParams {
	var ()
	return &CreatePipelineVersionParams{
		HTTPClient: client,
	}
}

/*CreatePipelineVersionParams contains all the parameters to send to the API endpoint
for the create pipeline version operation typically these are written to a http.Request
*/
type CreatePipelineVersionParams struct {

	/*PipelineID
	  Required input. ID of the parent pipeline.

	*/
	PipelineID string

	timeout    time.Duration
	Context    context.Context
	HTTPClient *http.Client
}

// WithTimeout adds the timeout to the create pipeline version params
func (o *CreatePipelineVersionParams) WithTimeout(timeout time.Duration) *CreatePipelineVersionParams {
	o.SetTimeout(timeout)
	return o
}

// SetTimeout adds the timeout to the create pipeline version params
func (o *CreatePipelineVersionParams) SetTimeout(timeout time.Duration) {
	o.timeout = timeout
}

// WithContext adds the context to the create pipeline version params
func (o *CreatePipelineVersionParams) WithContext(ctx context.Context) *CreatePipelineVersionParams {
	o.SetContext(ctx)
	return o
}

// SetContext adds the context to the create pipeline version params
func (o *CreatePipelineVersionParams) SetContext(ctx context.Context) {
	o.Context = ctx
}

// WithHTTPClient adds the HTTPClient to the create pipeline version params
func (o *CreatePipelineVersionParams) WithHTTPClient(client *http.Client) *CreatePipelineVersionParams {
	o.SetHTTPClient(client)
	return o
}

// SetHTTPClient adds the HTTPClient to the create pipeline version params
func (o *CreatePipelineVersionParams) SetHTTPClient(client *http.Client) {
	o.HTTPClient = client
}

// WithPipelineID adds the pipelineID to the create pipeline version params
func (o *CreatePipelineVersionParams) WithPipelineID(pipelineID string) *CreatePipelineVersionParams {
	o.SetPipelineID(pipelineID)
	return o
}

// SetPipelineID adds the pipelineId to the create pipeline version params
func (o *CreatePipelineVersionParams) SetPipelineID(pipelineID string) {
	o.PipelineID = pipelineID
}

// WriteToRequest writes these params to a swagger request
func (o *CreatePipelineVersionParams) WriteToRequest(r runtime.ClientRequest, reg strfmt.Registry) error {

	if err := r.SetTimeout(o.timeout); err != nil {
		return err
	}
	var res []error

	// path param pipeline_id
	if err := r.SetPathParam("pipeline_id", o.PipelineID); err != nil {
		return err
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}
